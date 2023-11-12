# Python consumer for the Flask API
import requests

# define endpoint
url = 'http://localhost:5000/get_data'

# define headers
# headers = {'Content-Type': 'application/json'}
# params = {'key': 'value'}

param = {"param1": "value1", "param2": "value2"}

# make request and print response

response = requests.get(url, params=param)

if response.status_code == 200:
    #convert to json
    data = response.json()
    # print data
    print(data)

else:
    print(" ERROR:",response.status_code)    
