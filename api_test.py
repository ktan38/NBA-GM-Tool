from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

client.get_contracts(
    output_type=OutputType.CSV, 
    output_file_path="./teamcontracts.csv"
)