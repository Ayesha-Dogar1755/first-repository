# program  to show methods of dictionary
my_dict = {
    "name": "Abeer",
    "age": 21,
    "city": "Riyadh"
}
# Display original dictionary
print("Original dictionary:", my_dict)
#show total keys:
print("Keys in the dictionary:", my_dict.keys())
#show total values:
print("Values in the dictionary:", my_dict.values())
#show total items:
print("Items in the dictionary:", my_dict.items())
# Get value for a specific key
print("Value for key 'name':", my_dict.get("name"))
# Check if a key exists
print("Is 'age' a key in the dictionary?", "age" in my_dict)
# Remove a key-value pair
removed_value = my_dict.pop("city", "Not Found")
print("Removed value for key 'city':", removed_value)