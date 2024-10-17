from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType, Team
from basketball_reference_web_scraper.html import SalariesPage
from basketball_reference_web_scraper.http_service import HTTPService 
import requests
from lxml import html



url = '{BASE_URL}/contracts/BOS.html'.format(
            BASE_URL=HTTPService.BASE_URL,
            
        )

response = requests.get(url=url, allow_redirects=False)

response.raise_for_status()

sp = SalariesPage(html=html.fromstring(response.content))

