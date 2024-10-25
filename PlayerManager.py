import requests

class PlayerManager:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_player_pool(self):
        response = requests.get(f"{self.api_url}/players")
        return response.json() if response.status_code == 200 else {}

    def create_player(self, player_id, name, position, team=None, tradeable=True, injury_status=None):
        data = {
            'player_id': player_id,
            'name': name,
            'position': position,
            'team': team,
            'tradeable': tradeable,
            'injury_status': injury_status
        }
        response = requests.post(f"{self.api_url}/player", json=data)
        return response.json() if response.status_code == 201 else response.text

    def update_player(self, player_id, **kwargs):
        response = requests.put(f"{self.api_url}/player/{player_id}", json=kwargs)
        return response.json() if response.status_code == 200 else response.text

    def update_all_players(self, **kwargs):
        """
        Updates certain attributes for all players.
        """
        player_pool = self.get_player_pool()
        for player_id in player_pool.keys():
            self.update_player(player_id, **kwargs)

    def remove_player(self, player_id):
        response = requests.delete(f"{self.api_url}/player/{player_id}")
        return response.json() if response.status_code == 200 else response.text

    def get_player(self, player_id):
        player_pool = self.get_player_pool()
        return player_pool.get(player_id, None)