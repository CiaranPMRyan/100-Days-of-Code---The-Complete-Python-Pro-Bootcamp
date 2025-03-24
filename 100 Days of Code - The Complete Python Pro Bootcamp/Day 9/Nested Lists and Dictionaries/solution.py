capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print Lille
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

# Nested dictionary in a dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

# print(travel_log["Germany"]["cities_visited"][2])


coins = {
    "quarter": {
        "value": 0.25,
        "amount": 0,
        "total": 0
    },
    "dime": {
        "value": 0.10,
        "amount": 0,
        "total": 0
    },
    "nickel": {
        "value": 0.05,
        "amount": 0,
        "total": 0
    },
    "cent": {
        "value": 0.01,
        "amount": 0,
        "total": 0
    },
}

coins_total = 0

for key in coins:
    coins[key]["amount"] = int(input(f"Please put in number of {key}: "))
    coins[key]["total"] = coins[key]["value"] * coins[key]["amount"]
    print(f"You have inserted {coins[key]["amount"]} {key}, {coins[key]["total"]}")
    coins_total += coins[key]["total"]

print(coins_total)