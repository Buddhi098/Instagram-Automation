import random
import os
from instagrapi import Client
import time
with open("valid_proxy.txt" , "r") as fi:
    line = fi.read().strip().split("\n")

with open("Instagram_accounts.txt" , "r") as f:
    lines = f.read().split("\n")
# add comment
comments = ["" , "looking gorgeous" , "Amazing"]

# impression count
n = 10

for i in range(10,12):
    x = random.randint(0,20)
    timeinterval = random.randint(1,15)
    username = lines[i].split(" ")[0]
    password = lines[i].split(" ")[1]
    proxy = line[x].split(" ")[0]
    user = line[x].split(" ")[1]
    client = Client()
    client.set_proxy(f"http://{user}@{proxy}")
    print(f"successfully connect proxy :{proxy} with user {username}")
    if os.path.exists(f"./session/session{i}.json") and os.path.getsize(f"./session/session{i}.json")>0:
        client.load_settings(f"./session/session{i}.json")
    try:
        client.login(username , password)
    except:
        print("Can't login account")
        continue
    client.dump_settings(f"./session/session{i}.json")
    id = client.media_pk_from_url("https://www.instagram.com/reel/CsdqwvoO45z/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==")
    # comment
    if(0):
        try:
            comment = client.media_comment(id , comments[i%3])
            print(f"comment from user {username}")
        except:
            print(f"Can't comment from user {username}")
    # like
    if(1):
        try:
            like = client.media_like(id)
            print(f"like from user {username}")
        except:
            print(f"Can't like from user {username}")
    # view
    if(1):
        try:
            seen = client.media_seen([id])
            print(f"Seen from user {username}")
        except:
            print(f"Can't Seen from user {username}")
    # saves
    if(1):
        try:
            save = client.media_save(id)
            print(f"Save from user {username}")
        except:
            print(f"Can't Save from user {username}")
    # follow
    if(0):
        # follow user
        try:
            userid = client.user_id_from_username("joannefdo")
            follow = client.user_follow(userid)
            print(f"follower by user {username}")
        except:
            print(f"Can't follower user by {username}")
        if(i==(n-1)):
                with open("example.txt", "w") as file:
                    # Write text to the file
                    file.write(f"follower count: {n}")
    print(f"wait for {timeinterval} seconds")
    time.sleep(timeinterval)
    