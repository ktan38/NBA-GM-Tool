from datetime import date

class PlayerContract:
    def __init__(self, duration, salary_per_year, team_options=None, player_options=None, incentives=None, contract_date=None):
        """
        Represents a player's contract details.
        :param duration: Number of years the contract lasts
        :param salary_per_year: List of salaries for each year of the contract
        :param team_options: Dictionary mapping specific years to booleans indicating team option (optional)
        :param player_options: Dictionary mapping specific years to booleans indicating player option (optional)
        :param incentives: Dictionary of incentives (e.g., bonuses for performance milestones)
        :param contract_date: Date when the contract was last signed or updated (optional)
        """
        self.duration = duration
        self.salary_per_year = salary_per_year
        self.team_options = team_options if team_options else {}
        self.player_options = player_options if player_options else {}
        self.incentives = incentives if incentives else {}
        self.contract_date = contract_date if contract_date else date.today()  # Default to today's date

        self._validate_options()

    def _validate_options(self):
        for year in self.team_options:
            if year in self.player_options:
                raise ValueError(f"Year {year} cannot have both a team option and a player option.")

    # Getters for contract details
    def get_duration(self):
        return self.duration

    def get_salary_per_year(self):
        return self.salary_per_year

    def get_team_options(self):
        return self.team_options

    def get_player_options(self):
        return self.player_options

    def get_incentives(self):
        return self.incentives

    def get_contract_date(self):
        return self.contract_date

    def get_total_value(self):
        return sum(self.salary_per_year)

    def __repr__(self):
        return (f"Duration: {self.duration} years, "
                f"Salaries: {self.salary_per_year}, "
                f"Team Options: {self.team_options}, "
                f"Player Options: {self.player_options}, "
                f"Incentives: {self.incentives}, "
                f"Contract Date: {self.contract_date}")