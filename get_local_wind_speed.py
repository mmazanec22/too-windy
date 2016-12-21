import requests
import sys
import time

# MAKE SURE LIMIT IS NOT EXCEEDED

# track total num calls and date of last call made; if current call is different date, then clear the total num of API calls

total_num_calls = 0
# date_last_call = TODAY SOMEHOW

def exceed_limit():
  if total_num_calls >= 1000:
    return true
  else:
    return false



# MAKE API CALL

def return_data_from_api(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()

# def get_current_wind_speed_from_return_data(json_data):
#   return json_data["wind"]["speed"]

def get_current_wind_speed_by_lat_lon(lat, lon):
  try:
    api_key = ""
    with open('dark_sky_api_key.txt', 'r') as myfile:
      api_key = myfile.read().replace('\n', '')
    url = "https://api.darksky.net/forecast/" + api_key + "/" + str(lat) +"," + str(lon)
    data = return_data_from_api(url)
    return data['hourly']['data']
  except:
    return "Do you even latitude and longitude, bro?"



# RUN THE WHOLE THING

hourly_data = get_current_wind_speed_by_lat_lon(sys.argv[1], sys.argv[2])
# print to text file:
  # current speed
  # highest speed before midnight tonight w/time
  # weather warnings
  # all speeds in next 24 hours w/times

for k in hourly_data:
  print(k['time'])
  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(k['time'])))
  print(k)
  print("**********")


# until time ends in 00:00:00, loop through and update highest wind speed

print(hourly_data[0]['windSpeed'])

# return current speed
# if we have not exceeded the 1000/day limit
  # run the script
  # if last API call was yesterday, reset date of last call
  # add one to num of calls made today
  # update last API call date
# else somehow return "Whoops, we exceeded the limit of our API!  Maybe send the dev some cash."
