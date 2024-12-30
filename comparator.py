import json

fers = "followers.json"
fing = "following.json"

followers_file = open(fers, "r")
following_file = open(fing, "r")

followers = json.load(followers_file)
following = json.load(following_file)

followers_list = [line["string_list_data"][0]["value"] for line in followers]
following_list = [line["string_list_data"][0]["value"] for line in following["relationships_following"]]

temp3 = []
for element in following_list:
    if element not in followers_list:
        temp3.append(element)

for x in temp3:
    print(x)