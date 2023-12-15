import json
import urllib.request
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

weakest_wind = 0
strongest_wind = 0
weak_location = ""
strong_location = ""
print(weather)
# checking wind in a list of dictionaries and
# using conditional statement creating new lists:
for event in weather:
   if event["wind"] < weakest_wind or weakest_wind == 0:
      weakest_wind = event["wind"]
      weak_location = event["location"]
   if event["wind"] > strongest_wind:
      strongest_wind = event["wind"]
      strong_location = event["location"]

wind_lapland = []
wind_middle_fi = []
wind_south_fi = []

# creatilng new lists of wind values depending on location:
for event in weather:
   if event["area"] == "lapland":
      wind_lapland.append(event["wind"])
   if event["area"] == "middle":
      wind_middle_fi.append(event["wind"])
   if event["area"] == "south":
      wind_south_fi.append(event["wind"])

# creating own function to calculate average amount of given numbers:
def average(numbers):
   total = sum(numbers)
   amount = len(numbers)
   result = total / amount
   result = round(result, 1)
   return result

# getting the average values using own funtion:
avr_wind_lapland = average(wind_lapland)
avr_wind_middle = average(wind_middle_fi)
avr_wind_south = average(wind_south_fi)

# printing results:
print(f"Strongest wind today at location: {strong_location}, {strongest_wind} m/s")
print(f"Weakest wind today at location: {weak_location}, {weakest_wind} m/s\n")
print(f"Average wind, Lapland: {avr_wind_lapland} m/s")
print(f"Average wind, Middle part of Finland: {avr_wind_middle} m/s")
print(f"Average wind, Southern Finland: {avr_wind_south} m/s")


