from . import PlayerContract

class Player:
    def __init__(self, name, position, team=None, tradeable=True, injury_status=None, contract=None):
        self.name = name
        self.position = position
        self.team = team
        self.tradeable = tradeable
        self.injury_status = injury_status
        self.contract = contract  # Instance of PlayerContract

    def update(self, **kwargs):
        if 'team' in kwargs:
            self.team = kwargs['team']
        if 'tradeable' in kwargs:
            self.tradeable = kwargs['tradeable']
        if 'injury_status' in kwargs:
            self.injury_status = kwargs['injury_status']

    def sign_new_contract(self, new_contract):
        """
        Allows the player to sign a new contract.
        :param new_contract: An instance of PlayerContract representing the new contract.
        """
        self.contract = new_contract
        print(f"{self.name} has signed a new contract: {self.contract}")

    def check_contract_date(self, db_contract):
        """
        Compares the contract stored with the player to the contract in the database by checking the contract date.
        :param db_contract: The contract from the database to compare against.
        :return: True if the contract dates match, False otherwise.
        """
        if self.contract and db_contract:
            return self.contract.get_contract_date() == db_contract.get_contract_date()
        return False

    def get_contract_details(self):
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
        contract_details = f"Contract: {self.contract}" if self.contract else "No contract"
        return (f"{self.name} (Position: {self.position}, Team: {self.team}, "
                f"Tradeable: {self.tradeable}, Injury Status: {self.injury_status}, {contract_details})")

# Example Usage:

# Create an old contract for a player
old_contract = PlayerContract(
    duration=3,
    salary_per_year=[41_000_000, 42_000_000, 43_000_000],
    team_options={2: True},
    player_options={3: True},
    incentives={"MVP Bonus": 1_000_000}
)

# Create a player with the old contract
lebron = Player(name="LeBron James", position="SF", team="Los Angeles Lakers", contract=old_contract)

# Print the player's details before the new contract
print(lebron)

# Create a new contract for the player
new_contract = PlayerContract(
    duration=4,
    salary_per_year=[45_000_000, 46_000_000, 47_000_000, 48_000_000],
    team_options={4: True},
    incentives={"Championship Bonus": 2_000_000}
)

# The player signs the new contract
lebron.sign_new_contract(new_contract)

# Print the player's details after signing the new contract
print(lebron)