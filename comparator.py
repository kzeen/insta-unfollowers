import json

followers = "followers.json"
following = "following.json"

followers_file = open(followers, "r")
following_file = open(following, "r")

followers_json = json.load(followers_file)
following_json = json.load(following_file)

followers_list = [line["string_list_data"][0]["value"] for line in followers_json]
following_list = [line["string_list_data"][0]["value"] for line in following_json["relationships_following"]]

unfollowed_list = []
for element in following_list:
    if element not in followers_list:
        unfollowed_list.append(element)

for unfollowed in unfollowed_list:
    print(unfollowed)

followers_file.close()
following_file.close()