class PlayerContract:
    def __init__(self, duration, salary_per_year, team_options=None, player_options=None, incentives=None):
        """
        Represents a player's contract details.
        :param duration: Number of years the contract lasts
        :param salary_per_year: List of salaries for each year of the contract
        :param team_options: Dictionary mapping specific years to booleans indicating team option (e.g., {2: True})
        :param player_options: Dictionary mapping specific years to booleans indicating player option (e.g., {3: True})
        :param incentives: Dictionary of incentives (e.g., bonuses for performance milestones)
        """
        self.duration = duration
        self.salary_per_year = salary_per_year  # List of salaries for each year
        
        # Initialize team and player options with None and check for conflicts
        self.team_options = team_options if team_options else {}
        self.player_options = player_options if player_options else {}

        self._validate_options()  # Ensure no conflicts between team and player options

        self.incentives = incentives if incentives else {}  # Incentives tied to performance or conditions

    def _validate_options(self):
        """
        Ensures that no year has both a team option and a player option.
        Raises a ValueError if a conflict is found.
        """
        for year in self.team_options:
            if year in self.player_options:
                raise ValueError(f"Year {year} cannot have both a team option and a player option.")

    def get_total_value(self):
        """
        Calculates the total value of the contract across all years.
        :return: Total contract value
        """
        return sum(self.salary_per_year)

    # Getters for attributes
    def get_duration(self):
        """
        Returns the duration of the contract in years.
        """
        return self.duration

    def get_salary_per_year(self):
        """
        Returns the list of salaries per year.
        """
        return self.salary_per_year

    def get_team_options(self):
        """
        Returns the dictionary of team options tied to specific years.
        """
        return self.team_options

    def get_player_options(self):
        """
        Returns the dictionary of player options tied to specific years.
        """
        return self.player_options

    def get_incentives(self):
        """
        Returns the dictionary of incentives in the contract.
        """
        return self.incentives

    def __repr__(self):
        """
        Returns a string representation of the player's contract.
        """
        return (f"Duration: {self.duration} years, "
                f"Salaries: {self.salary_per_year}, "
                f"Team Options: {self.team_options}, "
                f"Player Options: {self.player_options}, "
                f"Incentives: {self.incentives}")