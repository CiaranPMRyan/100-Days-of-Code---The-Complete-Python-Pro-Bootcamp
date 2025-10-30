# my_dict = {}
#
# print(my_dict)
#
# my_dict["Bug"] = "Bug entry"
# my_dict["Function"] = "Function entry"
# my_dict["Loop"] = "Loop function"
#
# print(my_dict)
#
# for key in my_dict:
#     print(key + ": " + my_dict[key])
#
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# print(capitals["France"])
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Frankfurt", "Stuttgart"],
# }
#
# print(travel_log["France"][1])
#
# nested_list = ["A", "B", ["C", "D"]]
#
# print(nested_list[2][1])
#
# travel_log = {
#     "France": {
#         "num_times_visited" : 8,
#         "cities_visited": ["Paris", "Lille", "Dijon"]
#     },
#     "Germany": {
#         "num_times_visited" : 10,
#         "cities_visited": ["Berlin", "Frankfurt", "Stuttgart"],
#     }
# }
#

# print(travel_log["Germany"]["cities_visited"][2])

def find_highest_bidder(bidding_dict):
    amount = max(bidding_dict, key=bidding_dict.get)
    winner = max(bidding_dict, key=bidding_dict.get)

    print(winner)


bids = {}
play = True
while play == True:
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))

    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    if should_continue == "no":
        find_highest_bidder(bids)
        play = False
