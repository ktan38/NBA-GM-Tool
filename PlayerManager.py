from . import Player


class PlayerManager:
    def __init__(self, player_pool):
        """
        Manages player creation and player pool.
        :param player_pool: A reference to the global player pool.
        """
        self.player_pool = player_pool

    def create_player(self, name, salary, contract_years, position, team=None, tradeable=True, injury_status=None):
        """
        Creates a new player and adds them to the global player pool.
        :param name: Name of the player
        :param salary: Salary of the player
        :param contract_years: Remaining contract years
        :param position: Position of the player (e.g., PG, SG, etc.)
        :param team: Team the player belongs to
        :param tradeable: Whether the player is tradeable
        :param injury_status: Player's injury status
        :return: Player object
        """
        # Check if the player already exists
        if name in self.player_pool:
            print(f"Player {name} already exists in the player pool.")
            return self.player_pool[name]
        
        # Create a new player and add to the pool
        player = Player(name, salary, contract_years, position, team=team, tradeable=tradeable, injury_status=injury_status)
        self.player_pool[name] = player
        print(f"Created new player: {name}")
        return player

    def update_player(self, name, **kwargs):
        """
        Updates an existing player's attributes in the global player pool.
        Only the attributes passed in via kwargs will be updated.
        :param name: Name of the player
        :param kwargs: Attributes to update (e.g., salary, contract_years, injury_status, etc.)
        :return: Updated player object, or None if player does not exist
        """
        # Check if the player exists in the pool
        if name not in self.player_pool:
            print(f"Player {name} does not exist in the player pool.")
            return None

        # Get the existing player
        player = self.player_pool[name]
        
        # Update the player's attributes using kwargs
        player.update(**kwargs)
        print(f"Updated player: {name}")
        return player