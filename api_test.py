from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType, Team
from basketball_reference_web_scraper.html import SalariesPage, StandingsPage
from basketball_reference_web_scraper.http_service import HTTPService 
import requests
from lxml import html



print(Team.NEW_YORK_KNICKS)

client.get_salaries(
    team=Team.NEW_YORK_KNICKS, 
    output_type=OutputType.CSV, 
    output_file_path="./NYK_SALARIES.csv"
)

# client.season_schedule(season_end_year=2018)