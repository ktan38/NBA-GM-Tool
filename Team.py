from enum import Enum
from . import PlayerManager
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