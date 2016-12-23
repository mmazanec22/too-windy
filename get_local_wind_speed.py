import requests
import sys
import time
from pygeocoder import Geocoder
from datetime import datetime
from dateutil import parser
import os


# env variable
API_KEY = os.environ['API_KEY']


# takes zip code as argument
zip = sys.argv[1]
coordinates = Geocoder.geocode(zip).coordinates
lat = coordinates[0]
lon = coordinates[1]
city = Geocoder.geocode(zip).city


# MAKE API CALL

def return_data_from_api(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()

def get_all_data(lat, lon):
  try:
    url = "https://api.darksky.net/forecast/" + API_KEY + "/" + str(lat) +"," + str(lon)
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
  return "The strongest wind in " + city + " today will be " + str(highest_speed) + " mph at about " + time_of_highest_speed + "."

def highest_speed_only(all_data):
  todays_data = hourly_data(all_data)
  highest_speed = 0.0
  current_day = get_day_from_hourly_record(todays_data[0])
  for k in todays_data:
    if k['windSpeed'] > highest_speed and current_day == get_day_from_hourly_record(k):
      highest_speed = k['windSpeed']
  return str(highest_speed)


# RUN THE WHOLE THING

f = open('last_call_file.txt', 'r+')
all_contents_array = f.read().split("\n")
total_num_calls = int(all_contents_array[3])
date_last_call = parser.parse(all_contents_array[4]).date()
right_now = datetime.utcnow().date()

if total_num_calls < 1000 or date_last_call < right_now:
  all_data = get_all_data(lat, lon)
  highest_speed = highest_speed_only(all_data)
  high_speed_string = get_highest_speed_before_midnight_with_time(all_data)
  warning = warnings(all_data)

  if date_last_call < right_now:
    total_num_calls = 1
  else:
    total_num_calls = total_num_calls + 1

  date_last_call = right_now

  f = open('last_call_file.txt', 'r+')
  f.write('{}\n{}\n{}\n{}\n{}\n'.format(highest_speed,high_speed_string,warning,total_num_calls,date_last_call))

else:
  error_message = "Whoops, we exceeded the limit of the API!  Maybe send the dev some cash."
  f = open('last_call_file.txt', 'r+')
  f.write('{}\n{}\n{}\n{}\n{}\n'.format("!",error_message,"   ",total_num_calls,date_last_call))