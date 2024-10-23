class TeamManager:
    def __init__(self, teams=None):
        """
        Manages all NBA teams and performs global updates (roster, payroll, etc.).
        :param teams: A dictionary of team objects, keyed by team name.
        """
        self.teams = teams if teams else {}

    def add_team(self, team):
        if team.name not in self.teams:
            self.teams[team.name] = team
            print(f"Team {team.name} has been added.")
        else:
            print(f"Team {team.name} already exists.")

    def remove_team(self, team_name):
        if team_name in self.teams:
            del self.teams[team_name]
            print(f"Team {team_name} has been removed.")
        else:
            print(f"Team {team_name} does not exist.")

    def update_all_teams(self):
        """
        Delegates the responsibility of updating rosters and payrolls to each team.
        Each team is responsible for its own roster and payroll updates.
        """
        for team_name, team in self.teams.items():
            print(f"Updating team: {team_name}")
            team.update_roster()  # Delegate to the team's own method
            team.update_payroll()  # Delegate to the team's own method
            print(f"{team_name} updated.")