import json
import urllib.request

# getting data from url:
url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather_condition = json.loads(raw_data)

city_list = {}
max_point = 0
city_max = ""

# check all items in the list and creating a new list of dictionaries
# where is a key is a city and a value is how many times it appeared in data:
for item in weather_condition:
    count = city_list.get(item["city"], 0) + 1
    if count > max_point:
        max_point = count
    city_list[item['city']] = city_list.get(item["city"], 0) + 1

# for-loop goes through a new list and finds city which has max point:
for city, number in city_list.items():
    if number == max_point:
        city_max += city + ","

# printing city which has the most warnings:
print(f"{city_max[:-1]} has(have) the most warnings of slippery weather conditions")

# sort data by time it was created:
weather_sorted = sorted(weather_condition, key=lambda x: x["created_at"], reverse=True)

# printing city, date and time from the last 5 dictionaries in a sorted list:
for city_info in weather_sorted[:5]:
    city = city_info["city"]
    date = city_info["created_at"]
    print(f"{city} {date}")









