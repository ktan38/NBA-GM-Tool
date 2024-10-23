from . import PlayerContract

class Player:
    def __init__(self, id,name, position, team=None, tradeable=True, injury_status=None, contract=None):
        self.id = id
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
        print(f"{self.name} (id = {self.id}) has signed a new contract: {self.contract}")

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

