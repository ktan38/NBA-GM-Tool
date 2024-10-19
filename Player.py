from . import PlayerContract

class Player:
    def __init__(self, name, position, team=None, tradeable=True, injury_status=None, contract=None):
        """
        Represents an NBA player.
        :param name: Player name
        :param position: Player's position (e.g., PG, SG, etc.)
        :param team: The team the player is currently assigned to
        :param tradeable: Boolean indicating if the player is eligible for trade
        :param injury_status: Any current or past injury status
        :param contract: Instance of PlayerContract that contains contract details
        """
        self.name = name
        self.position = position
        self.team = team
        self.tradeable = tradeable
        self.injury_status = injury_status
        self.contract = contract  # Instance of PlayerContract

    def update(self, **kwargs):
        """
        Updates the player's attributes based on the provided keyword arguments.
        Only updates the attributes passed in the kwargs; others remain unchanged.
        :param kwargs: Attributes to update (e.g., team, tradeable, injury_status)
        """
        if 'team' in kwargs:
            self.team = kwargs['team']
        if 'tradeable' in kwargs:
            self.tradeable = kwargs['tradeable']
        if 'injury_status' in kwargs:
            self.injury_status = kwargs['injury_status']

    def get_contract_details(self):
        """
        Returns the player's contract details by accessing the PlayerContract instance.
        """
        if self.contract:
            return {
                "duration": self.contract.get_duration(),
                "salary_per_year": self.contract.get_salary_per_year(),
                "team_options": self.contract.get_team_options(),
                "player_options": self.contract.get_player_options(),
                "incentives": self.contract.get_incentives(),
                "total_value": self.contract.get_total_value()
            }
        return None

    def __repr__(self):
        """
        Returns a string representation of the player, including contract details.
        """
        contract_details = f"Contract: {self.contract}" if self.contract else "No contract"
        return (f"{self.name} (Position: {self.position}, Team: {self.team}, "
                f"Tradeable: {self.tradeable}, Injury Status: {self.injury_status}, {contract_details})")


# Example Usage:

# Create a player contract with salary per year, team and player options, and incentives
lebron_contract = PlayerContract(
    duration=3,
    salary_per_year=[41_000_000, 42_000_000, 43_000_000],
    team_options={2: True},  # Team option in the second year
    player_options={3: True},  # Player option in the third year
    incentives={"MVP Bonus": 1_000_000, "All-Star Appearance": 500_000}
)

# Create a player with the contract
lebron = Player(name="LeBron James", position="SF", team="Los Angeles Lakers", contract=lebron_contract)

# Print player and contract details
print(lebron)

# Get contract details using the player's get_contract_details method
contract_details = lebron.get_contract_details()
print(f"Player Contract Details: {contract_details}")

# Example of updating the player's team
lebron.update(team="Miami Heat")
print(lebron)