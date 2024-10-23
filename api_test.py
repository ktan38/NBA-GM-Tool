from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

client.all_player_contracts(
    output_type=OutputType.CSV, 
   output_file_path="./allplayercontracts.csv"
)


