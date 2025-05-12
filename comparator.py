import json
from datetime import datetime

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

with open("unfollowed_" + datetime.today().strftime("%Y-%m-%d_%H-%M-%S") + ".txt", "w") as f:
    f.write("Number of followers: " + str(len(followers_list)) + "\n")
    f.write("Number of following: " + str(len(following_list)) + "\n\n")
    for unfollowed in unfollowed_list:    
        f.write(unfollowed + "\n\n")

followers_file.close()
following_file.close()