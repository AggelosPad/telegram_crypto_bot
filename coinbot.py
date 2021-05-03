

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import time

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'XXXXXXXXXXXX',
}

session = Session()
session.headers.update(headers)
coinname = str(input("Please enter a coin: "))
while(1):
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #mycoin = data('Bitcoin')
        with open("data_file.json", "w") as write_file:
            json.dump(data, write_file)

        
        #subprocess.call("datamessage.py", shell=True)
        command = 'python datamessage.py ' + str(coinname)
        print(command)
        os.system(command)  


    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    time.sleep(3600)