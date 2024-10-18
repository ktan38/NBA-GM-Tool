from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType, Team
from basketball_reference_web_scraper.html import SalariesPage, StandingsPage
from basketball_reference_web_scraper.http_service import HTTPService 
import requests
from lxml import html



# url = '{BASE_URL}/contracts/BOS.html'.format(
#             BASE_URL=HTTPService.BASE_URL,
            
#         )

# response = requests.get(url=url, allow_redirects=False)

# response.raise_for_status()

# sp = SalariesPage(html=html.fromstring(response.content))

# st = sp.salaries_table

# st.rows()




client.get_salaries(
    team="BOS", 
    output_type=OutputType.CSV, 
    output_file_path="./BOS_SALARIES.csv"
)

# client.season_schedule(season_end_year=2018)