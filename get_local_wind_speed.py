import requests
import sys

def return_data_from_api(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()

def get_wind_speed_from_return_data(json_data):
  return json_data["wind"]["speed"]

def get_current_wind_speed_by_zip(zip):
  try:
    url = "http://api.openweathermap.org/data/2.5/weather?zip=" + str(zip) + ",us"
    data = return_data_from_api(url)
    print(data)
    speed = get_wind_speed_from_return_data(data)
    return speed
  except:
    return "Do you even zip code, bro?"

print(get_current_wind_speed_by_zip(sys.argv[0]))