class TeamManager:
    def __init__(self, teams=None):
        """
        Manages all NBA teams and performs global updates (roster, payroll, etc.).
        :param teams: A dictionary of team objects, keyed by team name.
        """
        self.teams = teams if teams else {}  # Dictionary of team objects

    def add_team(self, team):
        """
        Adds a new team to the manager.
        :param team: The team object to be added.
        """
        if team.name not in self.teams:
            self.teams[team.name] = team
            print(f"Team {team.name} has been added to the manager.")
        else:
            print(f"Team {team.name} already exists in the manager.")

    def remove_team(self, team_name):
        """
        Removes a team from the manager.
        :param team_name: The name of the team to be removed.
        """
        if team_name in self.teams:
            del self.teams[team_name]
            print(f"Team {team_name} has been removed from the manager.")
        else:
            print(f"Team {team_name} does not exist in the manager.")

    def update_all_rosters(self):
        """
        Updates the rosters for all teams. This simulates a daily update for all teams.
        Each team is responsible for its own roster update logic.
        """
        for team_name, team in self.teams.items():
            print(f"Updating roster for {team_name}...")
            team.update_roster()  # Assumes each team has its own update_roster method
            print(f"Roster for {team_name} has been updated.")

    def update_all_payrolls(self):
        """
        Updates the payroll for all teams based on the current roster and contracts.
        """
        for team_name, team in self.teams.items():
            print(f"Updating payroll for {team_name}...")
            team.update_payroll()  # Assumes each team has its own update_payroll method
            print(f"Payroll for {team_name} has been updated.")

    def display_all_teams_info(self):
        """
        Displays information for all teams.
        """
        for team_name, team in self.teams.items():
            team.display_team_info()

    def get_all_teams(self):
        """
        Returns a list of all teams managed by the TeamManager.
        """
        return list(self.teams.values())
