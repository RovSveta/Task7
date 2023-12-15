# list of dictionaries:
restaurants = [
    {
        "name": "North Delish",
        "rating": 4.5,
        "reservations": True,
        "services": [
            "lunch",
            "dinner"
        ],
        "price_level": 5,
        "location":"Rovaniemi"
    },
    {
        "name": "Food Galore",
        "rating": 3.8,
        "reservations": False,
        "services": [
            "lunch",
            "breakfast"
        ],
        "price_level": 3,
        "location": "London"
    },
    {
        "name": "Snacksy Ltd",
        "rating": 3.2,
        "reservations": False,
        "services": [
            "lunch",
            "dinner",
            "night"
        ],
        "price_level": 2,
        "location": "Berlin"
    },
    {
        "name": "The Rock Restaurant",
        "rating": 4.1,
        "reservations": True,
        "services": [
            "breakfast",
            "lunch",
            "dinner",
            "night"
        ],
        "price_level": 3,
        "location": "Zanzibar"
    },
    {
        "name": "The Grotto",
        "rating": 4.9,
        "reservations": True,
        "services": [
            "breakfast",
            "lunch",
            "dinner"
        ],
        "price_level": 2,
        "location": "Krabi"
    },
    {
        "name": "The Labassin Waterfall Restaurant",
        "rating": 3.9,
        "reservations": True,
        "services": [
            "lunch",
            "dinner"
        ],
        "price_level": 3,
        "location": "San Pablo"
    },
    {
        "name": "Bird’s Nest Restaurant",
        "rating": 4.6,
        "reservations": False,
        "services": [
            "breakfast",
            "lunch",
            "dinner"
        ],
        "price_level": 4,
        "location": "Soneva Kiri Eco Resort"
    },
    {
        "name": "Huvafen Fushi",
        "rating": 3.3,
        "reservations": False,
        "services": [
            "lunch",
            "dinner",
            "night"
        ],
        "price_level": 1,
        "location": "North Malé"
    },
    {
        "name": "Huvafen Fushi 2",
        "rating": 3.3,
        "reservations": False,
        "services": [
            "lunch",
            "dinner",
            "night"
        ],
        "price_level": 1,
        "location": "North Malé"
    }]

# user input:
rating = int(input("Which star rating at least for the restaurant? (1-5)\n"))
price_client = int(input("What is the maximum price level you're looking for? (1-5)\n"))
reservation_client = input("Would you like to make a reservation before hand? (y/n)\n")
reservation_client = reservation_client == "y"
time = int(input("In what time would you like to arrive? (0 – 23)\n"))

restaurants_match = []
time_to_go = ""

# setting the needed service based on the user input:
if 6 <= time <= 10:
    time_to_go = "breakfast"
elif 11 <= time <= 16:
    time_to_go = "lunch"
elif 17 <= time <= 24:
    time_to_go = "dinner"
else:
    time_to_go = "night"

# finding the matching restaurant:
for restaurant in restaurants:
    if rating > restaurant["rating"]:
        # continue stops executing the code further and will switch to another restaurant:
        continue
    if price_client < restaurant["price_level"]:
        continue
    # y - True, n - False:
    if int(reservation_client) > int(restaurant["reservations"]):
        continue
    if time_to_go in restaurant["services"]:
        restaurants_match.append(restaurant["name"])

# join() for printing only the names of restaurants:
restaurants_to_go_str = ", ".join(restaurants_match)

# print handling:
if restaurants_match:
    print(restaurants_to_go_str)
else:
    print("No matching restaurants found, unfortunately!")
