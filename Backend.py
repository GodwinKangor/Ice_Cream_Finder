# from flask import Flask, jsonify, request,send_from_directory
# import googlemaps
# import requests
#
# app = Flask(__name__)
#
# API_KEY = open("API_KEY.txt", 'r').read().strip()
# map_client = googlemaps.Client(API_KEY)
#
# @app.route('/')
# def serve_frontend():
#     return send_from_directory(app.static_folder, 'Static/index.html')
#
# def get_user_location():
#     ip_address = requests.get('http://api.ipify.org').text
#     response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
#     return response['lat'], response['lon']
#
#
# @app.route('/ice_cream_places', methods=['GET'])
# def ice_cream_places():
#     lat, lng = get_user_location()
#     radius = request.args.get('radius', 1500)  # Default radius is 1500 meters
#
#     places_response = map_client.places_nearby(
#         location=(lat, lng),
#         radius=radius,
#         keyword='ice cream',
#         type='restaurant'
#     )
#
#     places = []
#     if places_response['status'] == 'OK':
#         for place in places_response['results']:
#             places.append({
#                 'name': place['name'],
#                 'location': place['geometry']['location'],
#             })
#
#     return jsonify(places)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request, send_from_directory
import googlemaps
import requests

app = Flask(__name__, static_folder='static')  # Set static folder path

API_KEY = open("API_KEY.txt", 'r').read().strip()
map_client = googlemaps.Client(API_KEY)

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

def get_user_location():
    ip_address = requests.get('http://api.ipify.org').text
    response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
    return response['lat'], response['lon']

@app.route('/ice_cream_places', methods=['GET'])
def ice_cream_places():
    lat, lng = get_user_location()
    radius = request.args.get('radius', 1500)  # Default radius is 1500 meters

    places_response = map_client.places_nearby(
        location=(lat, lng),
        radius=radius,
        keyword='ice cream',
        type='restaurant'
    )

    places = []
    if places_response['status'] == 'OK':
        for place in places_response['results']:
            places.append({
                'name': place['name'],
                'location': place['geometry']['location'],
            })

    return jsonify(places)

if __name__ == '__main__':
    app.run(debug=True)
