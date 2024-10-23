from . import Player

class PlayerManager:
    def __init__(self, player_pool):
        """
        Manages player creation and player pool.
        :param player_pool: A reference to the global player pool (dictionary keyed by player_id).
        """
        self.player_pool = player_pool

    def create_player(self, player_id, name, salary, contract_years, position, team=None, tradeable=True, injury_status=None):
        """
        Creates a new player and adds them to the global player pool.
        :param player_id: Unique ID for the player.
        :param name: Name of the player.
        :param salary: Player's salary.
        :param contract_years: Remaining contract years.
        :param position: Position of the player (e.g., PG, SG, etc.).
        :param team: Team the player belongs to.
        :param tradeable: Whether the player is tradeable.
        :param injury_status: Player's injury status.
        :return: Player object.
        """
        if player_id in self.player_pool:
            print(f"Player with ID {player_id} already exists in the player pool.")
            return self.player_pool[player_id]
        
        player = Player(player_id, name, salary, contract_years, position, team=team, tradeable=tradeable, injury_status=injury_status)
        self.player_pool[player_id] = player
        print(f"Created new player: {name} (ID: {player_id})")
        return player

    def update_player(self, player_id, **kwargs):
        """
        Updates an existing player's attributes and contract in the global player pool.
        Only the attributes passed in via kwargs will be updated.
        :param player_id: Unique ID of the player.
        :param kwargs: Attributes to update (e.g., salary, contract_years, injury_status, contract, etc.).
        :return: Updated player object, or None if the player does not exist.
        """
        if player_id not in self.player_pool:
            print(f"Player with ID {player_id} does not exist in the player pool.")
            return None

        player = self.player_pool[player_id]
        player.update(**kwargs)
        print(f"Updated player: {player.name} (ID: {player_id})")
        return player

    def update_all_players(self, **kwargs):
        """
        Globally updates certain attributes for all players in the player pool.
        Only the attributes passed in via kwargs will be updated.
        :param kwargs: Attributes to update (e.g., salary, injury_status, etc.).
        """
        for player in self.player_pool.values():
            player.update(**kwargs)
            print(f"Updated player: {player.name} (ID: {player.player_id})")

    def remove_player(self, player_id):
        """
        Removes a player from the global player pool.
        :param player_id: Unique ID of the player to remove.
        :return: True if removed, False if the player was not found.
        """
        if player_id in self.player_pool:
            del self.player_pool[player_id]
            print(f"Player with ID {player_id} has been removed from the player pool.")
            return True
        else:
            print(f"Player with ID {player_id} does not exist in the player pool.")
            return False

    def get_player(self, player_id):
        """
        Retrieves a player from the global player pool without modifying them.
        :param player_id: Unique ID of the player to retrieve.
        :return: Player object, or None if the player does not exist.
        """
        return self.player_pool.get(player_id, None)