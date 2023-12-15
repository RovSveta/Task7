# creating a list of inventory which contains other lists inside:

fruits = ["apple","pear","banana"]
berries = ["strawberry", "blueberry","blackberry"]
vegetables = ["carrot","kale","cucumber"]
inventory = [fruits, berries, vegetables]

# printing products using for-loop inside a foor-loop:
for products in inventory:
   for t in products:
      print(t)
