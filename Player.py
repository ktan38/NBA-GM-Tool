class Player:
    def __init__(self, name, salary, contract_years, position, team=None, tradeable=True, injury_status=None):
        """
        Represents an NBA player.
        :param name: Player name
        :param salary: Player's current salary
        :param contract_years: Number of years remaining on the contract
        :param position: Player's position (e.g., PG, SG, SF, PF, C)
        :param team: The team the player is currently assigned to
        :param tradeable: Boolean indicating if the player is eligible for trade
        :param injury_status: Any current or past injury status
        """
        self.name = name
        self.salary = salary
        self.contract_years = contract_years
        self.position = position
        self.team = team
        self.tradeable = tradeable
        self.injury_status = injury_status

    def update(self, **kwargs):
        """
        Updates the player's attributes based on the provided keyword arguments.
        Only updates the attributes passed in the kwargs; others remain unchanged.
        :param kwargs: Attributes to update (e.g., salary, contract_years, team, tradeable, injury_status)
        """
        if 'salary' in kwargs:
            self.salary = kwargs['salary']
        if 'contract_years' in kwargs:
            self.contract_years = kwargs['contract_years']
        if 'position' in kwargs:
            self.position = kwargs['position']
        if 'team' in kwargs:
            self.team = kwargs['team']
        if 'tradeable' in kwargs:
            self.tradeable = kwargs['tradeable']
        if 'injury_status' in kwargs:
            self.injury_status = kwargs['injury_status']

    def __repr__(self):
        """
        Returns a string representation of the player, useful for displaying player details.
        """
        return (f"{self.name} (${self.salary:,}, {self.contract_years} years remaining, "
                f"Position: {self.position}, Team: {self.team}, Tradeable: {self.tradeable}, "
                f"Injury Status: {self.injury_status})")