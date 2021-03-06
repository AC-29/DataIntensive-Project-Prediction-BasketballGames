import requests
import json
import time

MAX_CALLS = 60

parameters = {
    "per_page": 100,
    "page": 0,
}
session = requests.Session()
data = session.get("https://www.balldontlie.io/api/v1/players", params=parameters)
print(data.status_code)

json_file = data.json()
print(json_file['meta'])

data_list = []
for i in range(json_file['meta']['total_pages']):
    parameters = {
        "per_page": 100,
        "page": i,
    }
    if i == 0 or i % MAX_CALLS != 0:  # Inside the available api request window
        print("Request: " + str(i))
        aux = session.get("https://www.balldontlie.io/api/v1/games", params=parameters)
        assert aux.status_code == 200, "Status code is " + str(aux.status_code)
        data_list.append(aux.json())
    else:
        time.sleep(60)  # Wait for one minute and do other 60 API requests
        print("Request: " + str(i))
        aux = session.get("https://www.balldontlie.io/api/v1/games", params=parameters)
        assert aux.status_code == 200, "Status code is " + str(aux.status_code)
        data_list.append(aux.json())

with open('game_data.json', 'w') as f:
    json.dump(data_list, f)
