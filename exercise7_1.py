cafe = {
     "name": "Imaginary Cafe Ltd.",
     "website": "https://edu.frostbit.fi/sites/cafe/en",
     "categories": [
         "cafe",
         "tea",
         "lunch",
         "breakfast"
     ],
     "location": {
         "city": "Rovaniemi",
         "address": "Test address 22",
         "zip_code": "FI-96100"
     }
}

print(cafe["name"])
print(cafe["location"]["address"])
print(cafe["location"]["zip_code"],cafe["location"]["city"])
print("")
print(cafe["website"])

# 1 option: printing a list of services using join():
#services = ", ".join(cafe['categories'])
#print(f"Services: {services}")

# 2nd option: printing a list of services using for-loop:
services = ""
for items in cafe["categories"]:
        services = services + items + ", "

# deleting a comma after the last word:
text = services[:-2]

print(f"Services: {text}")

