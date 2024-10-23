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
        if id in self.player_pool:
            print(f"Player {self.player_pool[id].name} ({id}) already exists in the player pool.")
            return self.player_pool[id]
        
        # Create a new player and add to the pool
        player = Player(id, name, salary, contract_years, position, team=team, tradeable=tradeable, injury_status=injury_status)
        self.player_pool[id] = player
        print(f"Created new player: {name} (id = {id})")
        return player

    def update_player(self, id, **kwargs):
        """
        Updates an existing player's attributes and contract in the global player pool.
        Only the attributes passed in via kwargs will be updated.
        :param name: Name of the player
        :param kwargs: Attributes to update (e.g., salary, contract_years, injury_status, contract, etc.)
        :return: Updated player object, or None if player does not exist
        """
        if id not in self.player_pool:
            print(f"Player {id} does not exist in the player pool.")
            return None

        player = self.player_pool[id]
        player.update(**kwargs)
        print(f"Updated player: {id}")
        return player

    def update_all_players(self, **kwargs):
        """
        Globally updates certain attributes for all players in the global player pool.
        Only the attributes passed in via kwargs will be updated for every player.
        :param kwargs: Attributes to update (e.g., salary, contract_years, injury_status, contract, etc.)
        """
        for player in self.player_pool.values():
            player.update(**kwargs)
            print(f"Updated player: {player.name} (id = {player.id})")

    def remove_player(self, id):
        """
        Removes a player from the global player pool.
        :param name: Name of the player to remove
        :return: True if removed, False if the player was not found
        """
        if id in self.player_pool:
            del self.player_pool[id]
            print(f"Player {id} has been removed from the player pool.")
            return True
        else:
            print(f"Player {id} does not exist in the player pool.")
            return False

    def get_player(self, id):
        """
        Retrieves a player from the global player pool without modifying them.
        :param name: Name of the player to retrieve
        :return: Player object, or None if the player does not exist
        """
        return self.player_pool.get(id, None)