class Player:
    def __init__(self, player_id, name, position, team=None, tradeable=True, injury_status=None, contract=None):
        """
        Represents an NBA player.
        :param player_id: Unique ID for the player.
        :param name: Name of the player.
        :param salary: Player's salary.
        :param contract_years: Number of years left in the player's contract.
        :param position: The position the player plays (e.g., PG, SG, etc.).
        :param team: The team the player belongs to.
        :param tradeable: Whether the player is tradeable.
        :param injury_status: Player's injury status.
        :param contract: Instance of PlayerContract representing the player's contract.
        """
        self.player_id = player_id  # Unique identifier for the player
        
        self.name = name

        self.position = position
        self.team = team
        self.tradeable = tradeable
        self.injury_status = injury_status
        self.contract = contract

        #age
        #height
        #weight
        #years in nba
        #draft
        #stats
        #bird rights
        #trade restriction
        #qualifying offer

    def update(self, **kwargs):
        """
        Updates player attributes based on the provided keyword arguments.
        :param kwargs: Attributes to update.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Invalid attribute: {key}")

    def sign_new_contract(self, new_contract):
        """
        Signs a new contract and replaces the old one.
        :param new_contract: Instance of PlayerContract representing the new contract.
        """
        self.contract = new_contract

    def get_contract_details(self):
        """
        Returns the player's contract details.
        """
        return self.contract.get_details() if self.contract else "No contract"

    def __repr__(self):
        """
        Returns a string representation of the player.
        """
        contract_status = f"Contract: {self.get_contract_details()}" if self.contract else "No contract"
        return f"Player {self.player_id}: {self.name}, {self.position}, Team: {self.team}, {contract_status}"