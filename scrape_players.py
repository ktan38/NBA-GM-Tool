import requests
from lxml import html
import csv
import string

# Base URL for the players pages
base_url = 'https://www.basketball-reference.com/players/'

# List of letters a to z
letters = list(string.ascii_lowercase)

# Open the CSV file to write the data for all letters
with open('player_data_append_csv_all.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header for the CSV
    writer.writerow([
        'data-append-csv', 'player_name', 'year_min', 'year_max', 'pos', 'height', 'weight', 'birth_date', 'colleges'
    ])

    # Loop through each letter in the alphabet
    for letter in letters:
        # Build the URL for the current letter
        url = f'{base_url}{letter}/'

        # Send a request to the page
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            tree = html.fromstring(response.content)
            
            # Find all player rows by extracting th elements where data-stat="player"
            players = tree.xpath('//th[@data-stat="player"]')
            
            # Loop through each player row
            for player in players:
                # Extract the 'data-append-csv' value from the <th> tag
                data_append_csv = player.xpath('./@data-append-csv')[0] if player.xpath('./@data-append-csv') else ''

                # Extract the player's name:
                # 1. Check if the <a> is directly inside the <th>
                # 2. If not found, check if it's inside a <strong> tag (for active players)
                player_name = player.xpath('./a/text()')
                if not player_name:
                    player_name = player.xpath('./strong/a/text()')
                player_name = player_name[0] if player_name else ''
                
                # Move to the parent row to find corresponding td elements
                parent_row = player.getparent()

                # Extract the values for the various data-stat attributes
                year_min = parent_row.xpath('.//td[@data-stat="year_min"]/text()')[0] if parent_row.xpath('.//td[@data-stat="year_min"]/text()') else ''
                year_max = parent_row.xpath('.//td[@data-stat="year_max"]/text()')[0] if parent_row.xpath('.//td[@data-stat="year_max"]/text()') else ''
                pos = parent_row.xpath('.//td[@data-stat="pos"]/text()')[0] if parent_row.xpath('.//td[@data-stat="pos"]/text()') else ''
                height = parent_row.xpath('.//td[@data-stat="height"]/text()')[0] if parent_row.xpath('.//td[@data-stat="height"]/text()') else ''
                weight = parent_row.xpath('.//td[@data-stat="weight"]/text()')[0] if parent_row.xpath('.//td[@data-stat="weight"]/text()') else ''
                
                # Extract the birth_date (text inside <a> if exists, otherwise from <td>)
                birth_date = parent_row.xpath('.//td[@data-stat="birth_date"]/a/text()')[0] if parent_row.xpath('.//td[@data-stat="birth_date"]/a/text()') else parent_row.xpath('.//td[@data-stat="birth_date"]/text()')[0] if parent_row.xpath('.//td[@data-stat="birth_date"]/text()') else ''
                
                # Extract the colleges (text inside <a> if exists, otherwise from <td>)
                colleges = parent_row.xpath('.//td[@data-stat="colleges"]/a/text()')[0] if parent_row.xpath('.//td[@data-stat="colleges"]/a/text()') else parent_row.xpath('.//td[@data-stat="colleges"]/text()')[0] if parent_row.xpath('.//td[@data-stat="colleges"]/text()') else ''
                
                # Write the extracted data to the CSV
                writer.writerow([data_append_csv, player_name, year_min, year_max, pos, height, weight, birth_date, colleges])

            print(f"Data from {url} has been processed.")
        else:
            print(f"Failed to retrieve the webpage for letter {letter}. Status code: {response.status_code}")

print("All data has been exported to player_data_append_csv_all.csv")