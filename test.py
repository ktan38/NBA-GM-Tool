from app import app, db, Player  # Import your app, db, and Player model from app.py

# Set up an application context to interact with the database
with app.app_context():
    # Check if the player already exists
    existing_player = Player.query.filter_by(player_id="dummy_001").first()
    if not existing_player:
        dummy_player = Player(
            player_id="dummy_001",
            name="John Doe",
            position="PG",
            team="Example Team",
            tradeable=True,
            injury_status="Healthy"
        )
        db.session.add(dummy_player)
        db.session.commit()
        print("Dummy player added successfully.")
    else:
        print("Player already exists.")

    # Fetch and display all players
    players = Player.query.all()
    for player in players:
        print({
            "player_id": player.player_id,
            "name": player.name,
            "position": player.position,
            "team": player.team,
            "tradeable": player.tradeable,
            "injury_status": player.injury_status
        })