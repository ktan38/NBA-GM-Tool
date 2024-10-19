from enum import Enum
from . import PlayerManager, DraftPick
import requests
from basketball_reference_web_scraper.data import SalaryThresholds, TeamStatus

class Team:
    def __init__(self, name, player_manager, roster=None, payroll=0, cap_status=TeamStatus.UNDER_THE_CAP, available_exceptions=None):
        """
        Represents an NBA team.
        :param player_manager: Instance of PlayerManager to handle player creation and updates.
        """
        self.name = name
        self.roster = roster if roster else []  # List of Player objects
        self.payroll = payroll  # Total salary of the team's roster
        self.cap_status = cap_status  # Current cap status (using TeamStatus Enum)
        self.available_exceptions = available_exceptions if available_exceptions else {}  # Exceptions team has
        self.player_manager = player_manager  # Reference to player manager to handle player creation and updates
        self.draft_picks = self._initialize_draft_picks()  # Tracker for draft picks



    def _initialize_draft_picks(self):
        """
        Initializes draft picks for the team. Each team starts with its own round 1 and round 2 picks for future years.
        :return: Dictionary of draft picks, organized by year and round
        """
        draft_picks = {}
        for year in range(2024, 2030):  # Assuming we're tracking picks for 2024 to 2030
            draft_picks[year] = {
                1: DraftPick(year, 1, self.name),  # Round 1 pick
                2: DraftPick(year, 2, self.name)   # Round 2 pick
            }
        return draft_picks

    def add_traded_pick(self, year, round, from_team, protections=None):
        """
        Adds a traded draft pick to the team's draft pick tracker.
        :param year: Year of the draft
        :param round: Round of the pick (1 or 2)
        :param from_team: The team that originally owned the pick
        :param protections: Any protections attached to the pick (e.g., top-10 protected)
        """
        new_pick = DraftPick(year, round, current_team=self.name, origin_team=from_team, protections=protections)
        self.draft_picks[year][round] = new_pick
        print(f"Added traded {year} Round {round} pick from {from_team} with protections: {protections}")

    def trade_draft_pick(self, year, round, to_team, protections=None):
        """
        Trades the team's draft pick to another team and updates its protections if any.
        :param year: Year of the draft pick being traded
        :param round: Round of the draft pick being traded (1 or 2)
        :param to_team: The team receiving the draft pick
        :param protections: Protections on the pick (if any)
        """
        if year in self.draft_picks and round in self.draft_picks[year]:
            draft_pick = self.draft_picks[year][round]
            draft_pick.set_current_team(to_team)  # Update the current team using the setter
            if protections:
                draft_pick.set_protections(protections)  # Update protections if provided
            print(f"Traded {year} Round {round} pick to {to_team}. New protections: {protections}")
        else:
            print(f"Draft pick for {year} Round {round} not found.")

    def get_draft_picks(self):
        """
        Returns a list of all draft picks the team owns.
        """
        picks = []
        for year, rounds in self.draft_picks.items():
            for round, pick in rounds.items():
                picks.append(pick)
        return picks

    def print_draft_picks(self):
        """
        Prints all the draft picks the team owns.
        """
        print(f"Draft Picks for {self.name}:")
        for pick in self.get_draft_picks():
            print(f"- {pick}")



    def fetch_roster_from_api(self):
        """
        Fetches the latest roster data from the API for the given team.
        """
        try:
            response = requests.get(f"{self.API_URL}/{self.name.lower()}/roster")
            if response.status_code == 200:
                return response.json()  # Assuming the response is in JSON format
            else:
                print(f"Failed to fetch roster for {self.name}. Status Code: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching data from API: {e}")
            return []

    def update_roster(self):
        """
        Updates the team's roster by pulling the latest data from the API and only applying changes if needed.
        """
        roster_data = self.fetch_roster_from_api()
        if not roster_data:
            print(f"Could not update the roster for {self.name}.")
            return
        
        new_roster = []  # Temporary list to hold updated player objects
        new_payroll = 0  # Temporary variable for updated payroll
        
        for player_data in roster_data:
            name = player_data.get("name")
            salary = player_data.get("salary")
            contract_years = player_data.get("contract_years")
            position = player_data.get("position")
            tradeable = player_data.get("tradeable", True)
            injury_status = player_data.get("injury_status", None)
            
            # Check if the player exists in the global pool
            if name in self.player_manager.player_pool:
                # Update the player attributes using the update_player method
                player = self.player_manager.update_player(name, team=self.name)
            else:
                # Create a new player if they do not exist
                player = self.player_manager.create_player(name, salary, contract_years, position, team=self.name, tradeable=tradeable, injury_status=injury_status)
            
            # Add player to the team's updated roster
            new_roster.append(player)
            new_payroll += player.salary
        
        # Compare the new roster with the current roster
        if self.has_roster_changed(new_roster):
            self.roster = new_roster
            self.payroll = new_payroll
            self.update_cap_status()  # Update cap status based on the new payroll
            print(f"Roster for {self.name} has been updated.")
        else:
            print(f"No changes to the roster for {self.name}.")

    def has_roster_changed(self, new_roster):
        """
        Compares the current roster with the new roster to see if any changes are needed.
        """
        if len(new_roster) != len(self.roster):
            return True
        current_player_names = {player.name for player in self.roster}
        new_player_names = {player.name for player in new_roster}
        return current_player_names != new_player_names

    def update_cap_status(self):
        """
        Updates the team's cap status based on current payroll, using the TeamStatus and SalaryThresholds enum.
        """
        if self.payroll < SalaryThresholds.SALARY_CAP.value:
            self.cap_status = TeamStatus.UNDER_THE_CAP
        elif SalaryThresholds.SALARY_CAP.value <= self.payroll < SalaryThresholds.LUXURY_TAX.value:
            self.cap_status = TeamStatus.OVER_THE_CAP_UNDER_LUXURY_TAX
        elif SalaryThresholds.LUXURY_TAX.value <= self.payroll < SalaryThresholds.FIRST_APRON.value:
            self.cap_status = TeamStatus.LUXURY_TAX_PAYER
        elif SalaryThresholds.FIRST_APRON.value <= self.payroll < SalaryThresholds.SECOND_APRON.value:
            self.cap_status = TeamStatus.OVER_FIRST_APRON
        else:
            self.cap_status = TeamStatus.OVER_SECOND_APRON
    
    def print_roster(self):
        """
        Prints the current roster of the team.
        """
        print(f"Team: {self.name}")
        print("Current Roster:")
        for player in self.roster:
            print(f"- {player}")
    
    def display_team_info(self):
        """
        Displays general team info, including roster, payroll, and cap status.
        """
        print(f"Team: {self.name}")
        print(f"Payroll: ${self.payroll:,}")
        print(f"Cap Status: {self.cap_status.value}")
        print("Available Exceptions:")
        for exception, value in self.available_exceptions.items():
            print(f"- {exception}: ${value:,}")
        print("\nRoster:")
        self.print_roster()
        print("\nDraft Picks:")
        self.print_draft_picks()

# Example usage
if __name__ == "__main__":
    # Global player pool
    NBA_PLAYER_POOL = {}

    # Create a PlayerManager instance
    player_manager = PlayerManager(NBA_PLAYER_POOL)
    
    # Create an example team
    lakers = Team("Los Angeles Lakers", player_manager=player_manager, available_exceptions={"Non-Taxpayer MLE": 12_400_000})
    
    # Update the roster using the API (only applies changes if the roster has changed)
    lakers.update_roster()
    
    # Display team information
    lakers.display_team_info()