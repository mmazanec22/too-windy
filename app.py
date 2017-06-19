import os
import requests
import sys
import time

from datetime import datetime
from dateutil import parser
from flask import render_template
from pygeocoder import Geocoder


# TODO: find a better way to track num of calls made today-- limit at 999


app = Flask(__name__, instance_relative_config=True)

with app.app_context():
    # get API key

@app.route('/', methods = ['GET', 'POST'])
def index():
    zip_code = "60618"
    mph = 15.0

    if request.method == 'GET':
        # figure out how to get a user's zip code
        pass
    else:
        zip_code = request.form['input_zip']
        mph = request.form['input_mph']

    coordinates = Geocoder.geocode(zip_code).coordinates
    lat = coordinates[0]
    lon = coordinates[1]
    city = Geocoder.geocode(zip_code).city
    # render index.html with those variables

    try:
        url = "https://api.darksky.net/forecast/" + api_key + "/" + str(lat) +"," + str(lon)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

    return render_template('index.html', high_speed=high_speed)


def current_wind_speed(all_data):
    return all_data.get('hourly').get('data')[0]['windSpeed']

def get_day_from_hourly_record(input_record):
    return time.strftime('%d', time.localtime(input_record['time']))

def get_highest_speed_before_midnight_with_time(all_data):
    todays_data = all_data.get('hourly').get('data')
    highest_speed = 0.0
    time_of_highest_speed = ""
    current_day = get_day_from_hourly_record(todays_data[0])
    for k in todays_data:
        if k['windSpeed'] > highest_speed and current_day == get_day_from_hourly_record(k):
            highest_speed = k['windSpeed']
            time_of_highest_speed = time.strftime('%H:%M', time.localtime(k['time']))
    return "The strongest wind in " + city + " today will be " + str(highest_speed) + " mph at about " + time_of_highest_speed + "."

def highest_speed_only(all_data):
    todays_data = all_data.get('hourly').get('data')
    highest_speed = 0.0
    current_day = get_day_from_hourly_record(todays_data[0])
    for k in todays_data:
        if k['windSpeed'] > highest_speed and current_day == get_day_from_hourly_record(k):
            highest_speed = k['windSpeed']
    return str(highest_speed)

if __name__ == '__main__':
    app.run()
