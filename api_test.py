from basketball_reference_web_scraper import client


player_stats = client.player_box_scores(day=1, month=1, year=2017)

print(player_stats)