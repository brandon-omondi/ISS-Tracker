import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("We currently have " + 
           str(result["number"]) + " astronauts on the ISS. \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")
#Print Long & Lat
g = geocoder.ip('me')

file.write("\n Your current lat/long is:" + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

#set up world map
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180,-90,180,90)

#loading map Image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup() 

while True:
    #load current status of the ISS in real time. 
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #Extract coordinates
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    #OutPut to the terminal
    lat = float(lat)
    lon = float(lon)

    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    #update position of the ISS
    iss.goto(lon, lat)

    #refresh every 2 seconds
    time.sleep(2)

    #comments to test
