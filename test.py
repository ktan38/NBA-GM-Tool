import requests

# Add a player
data = {
    "player_id": "1",
    "name": "LeBron James",
    "position": "SF",
    "team": "Lakers",
    "tradeable": True,
    "injury_status": "Healthy"
}
response = requests.post("http://127.0.0.1:5000/player", json=data)
print(response.json())

# Get all players
response = requests.get("http://127.0.0.1:5000/players")
print(response.json())