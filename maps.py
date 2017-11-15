import googlemaps
import arrow

now = arrow.now()
print(now)

gmaps = googlemaps.Client(key = 'AIzaSyAl4XHRqKiWlAGllgyPRiJsFy1MYpzCvlQ')

directions = gmaps.directions("Impact Hub, Av. Álvaro Obregón 168", "Calle Séneca 148", mode = 'driving', departure_time=now)
print(directions)
'''
API_KEY = "AIzaSyAl4XHRqKiWlAGllgyPRiJsFy1MYpzCvlQ"
URL = "https://maps.googleapis.com/maps/api/directions/json?origin=75+9th+Ave+New+York,+NY&destination=MetLife+Stadium+1+MetLife+Stadium+Dr+East+Rutherford,+NJ+07073&key="
'''