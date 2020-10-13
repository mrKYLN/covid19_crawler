import requests
import bs4
from mysql_connector import MYSQL_CONNECTOR
import sys


request = requests.get("https://www.worldometers.info/coronavirus/")
data = request.text
soup = bs4.BeautifulSoup(data, 'html.parser')

continent_div= soup.find('li' , id="nav-na-tab")
continent = continent_div.text

location_div = soup.find('a', { "class" : "mt_a"})
location = location_div.text

total_case_div= soup.find_all('tr')[9].find_all('td')[2].text

"""


connector = MYSQL_CONNECTOR()
query = "INSERT INTO c_data (continent,location, date) VALUES ('{}','{}', now());".format(continent,location)
print(query)
connector.run_mysql_query(query)
print("{} works successfully!".format(query))
if (connector.CONNECTON.is_connected()):
    connector.CONNECTON.close()
    print("MySQL connection is closed")
    sys.exit(1)"""