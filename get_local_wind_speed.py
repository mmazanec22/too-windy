import requests
import sys
import time



# modify this to take a zip code arg rather than lat lon - need to use some converter


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
  except:
    return "Do you even latitude and longitude, bro?"



# PARSE DATA

def current_wind_speed(all_data):
  return all_data['hourly']['data'][0]['windSpeed']

# def warnings:
  # there's a warning somewhere in "all data"

def hourly_data(all_data):
  return data['hourly']['data']

def get_highest_speed_before_midnight_with_time(all_data):
  highest_speed = 0.0
  time_of_highest_speed = ""
  # modify this so it only looks at times before midnight - until time ends in 00:00:00
  for k in all_data['hourly']['data']:
    if k['windSpeed'] > highest_speed:
      highest_speed = k['windSpeed']
      time_of_highest_speed = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(k['time']))
  return "The strongest wind today will be " + str(highest_speed) + " at " + time_of_highest_speed



# MAKE SURE LIMIT IS NOT EXCEEDED

# track total_num_calls and date_last_call in a text file
# if current call is different date, then clear the total num of API calls

def exceed_limit():
  if total_num_calls >= 1000:
    return true
  else:
    return false



# RUN THE WHOLE THING

all_data = get_all_data_by_lat_lon(sys.argv[1], sys.argv[2])
# print to text file:
  # current speed
  # highest speed before midnight tonight w/time
  # weather warnings
  # all speeds in next 24 hours w/times



# return current speed
# if we have not exceeded the 1000/day limit
  # run the script
  # if last API call was yesterday, reset date of last call
  # add one to num of calls made today
  # update last API call date
# else somehow return "Whoops, we exceeded the limit of our API!  Maybe send the dev some cash."
