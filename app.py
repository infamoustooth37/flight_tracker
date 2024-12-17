from operator import index

from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

api_key = os.getenv('AVIATION_API_KEY')


@app.route('/')
def hello_world():
    params = {
        'access_key': api_key
    }

    api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

    api_response = api_result.json()

    flights_res = api_response['data']
    print(flights_res)


    # put application's code here
    return render_template('index.html', flights=flights_res)

@app.get('/api/find_flights')
def find_flights():
    airline_code = request.args.get('airline_code')
    params = {
        'access_key': api_key,
        'airline_icao': airline_code,
        'flight_status': 'active'

    }

    api_result = requests.get('https://api.aviationstack.com/v1/flights?search', params)

    api_response = api_result.json()

    flights_res = api_response['data']

    return render_template('flight_list.html', flights=flights_res)




if __name__ == '__main__':
    app.run()
