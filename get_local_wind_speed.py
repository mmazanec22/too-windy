import requests
import sys
import time
from pygeocoder import Geocoder



# takes zip code as argument
coordinates = Geocoder.geocode(sys.argv[1]).coordinates
lat = coordinates[0]
lon = coordinates[1]



# MAKE API CALL

def return_data_from_api(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()

def get_all_data(lat, lon):
  try:
    api_key = ""
    with open('dark_sky_api_key.txt', 'r') as myfile:
      api_key = myfile.read().replace('\n', '')
    url = "https://api.darksky.net/forecast/" + api_key + "/" + str(lat) +"," + str(lon)
    data = return_data_from_api(url)
    return data
  except:
    return "Do you even latitude and longitude, bro?"



# PARSE DATA

def current_wind_speed(all_data):
  return all_data['hourly']['data'][0]['windSpeed']

def warnings(all_data):
  if 'alerts' in all_data:
    return all_data['alerts']['title']
  else:
    return "No alerts for now!"

def hourly_data(all_data):
  return all_data['hourly']['data']

def get_day_from_hourly_record(input_record):
  return time.strftime('%d', time.localtime(input_record['time']))

def get_highest_speed_before_midnight_with_time(all_data):
  todays_data = hourly_data(all_data)
  highest_speed = 0.0
  time_of_highest_speed = ""
  current_day = get_day_from_hourly_record(todays_data[0])
  for k in todays_data:
    if k['windSpeed'] > highest_speed and current_day == get_day_from_hourly_record(k):
      highest_speed = k['windSpeed']
      time_of_highest_speed = time.strftime('%H:%M', time.localtime(k['time']))
  return "The strongest wind today will be " + str(highest_speed) + " MPH at about " + time_of_highest_speed



# MAKE SURE LIMIT IS NOT EXCEEDED

# track total_num_calls and date_last_call in a text file
# if current call is different date, then clear the total num of API calls

def exceed_limit():
  if total_num_calls >= 1000:
    return true
  else:
    return false



# RUN THE WHOLE THING

def print_to_file():
  f = open('last_call_file.txt', 'r+')
  all_data = get_all_data(lat, lon)
  curr_speed = current_wind_speed(all_data)
  high_speed = get_highest_speed_before_midnight_with_time(all_data)
  warning = warnings(all_data)
  f.write('{}\n{}\n{}\n'.format(curr_speed,high_speed,warning))

print_to_file()

# if we have not exceeded the 1000/day limit
  # run the method that prints to text file
  # if last API call was yesterday, reset date of last call in tracker text file
  # add one to num of calls made today in tracker text file
  # update last API call date in tracker text file
# else somehow return "Whoops, we exceeded the limit of our API!  Maybe send the dev some cash."
