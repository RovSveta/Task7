shopcart = [
     {"name": "Beehive - lamp", "price": 999.9},
     {"name": "Malm - bed", "price": 169.9},
     {"name": "Moomin - mug set", "price": 59.9},
     {"name": "Nemo - divan", "price": 699.9},
     {"name": "Ritz - armchair", "price": 369.9}
]

total_sum = 0
print("Receipt:")

# for-loop prints the name from  list of dictionaries:
for item in shopcart:
    total_sum = total_sum +item["price"]
    product = item["name"]
    print(f"- {product}")

# calculating VAT from price that already has VAT:
price_no_vat = total_sum/1.24
vat = round(total_sum - price_no_vat,1)

# print an empty line:
print()

#printing  total sum amount,an empty line after and coma again text:
print(f"Total sum: {total_sum} €.\nPlease come again!")

# printing amount of VAT:
print(f"VAT: {vat} €.")
