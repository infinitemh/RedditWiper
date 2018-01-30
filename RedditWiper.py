# Script to delete your comment history.

import praw
import time
import datetime

# login parameters. adjust as necessary.
# client_id and client_secret can be obtained by creating an app entry in (https://www.reddit.com/prefs/apps/)
# http://localhost:8080 is fine for redirect uri if you declare that it's a script application
# store this in a separate file and call from it if you won't be running it from your own machine. ex. configparser

username = "username"
password = "password"
client_id = "client_id"
client_secret = "client_secret"

# Login function. Creates a Reddit instance. Will be assigning it to r.
def bot_login():
    login = praw.Reddit(username=username,
                    password=password,
                    client_id=client_id,
                    client_secret=client_secret,
                    user_agent='InfiniteMH\'s /r/NBA Trade Bot', )
    return login


r = bot_login()


def delete_comments(count=None):
    comments_listobj = r.user.me().comments.new(limit=count)
    for comment in comments_listobj:
        print('Deleting :', comment.body)
        print('Posted on: ', datetime.datetime.fromtimestamp(int(comment.created)))
        comment.delete()
        print('Deleted. \n')
        # time.sleep(2) - a 2 sec delay between deletion because of Reddit's 30 requests per minute restriction.
        time.sleep(2)

def delete_posts(count=None):
    submissions_listobj = r.user.me().submissions.new(limit=count)
    for submission in submissions_listobj:
        print('Deleting : ', submission.title)
        print('Submitted on: ', datetime.datetime.fromtimestamp(int(submission.created)))
        submission.delete()
        print('Deleted. \n')
        time.sleep(2)


# Run the function you wish to run with the desired number of posts/comments. Nothing will delete ALL.
delete_comments()
delete_posts(3)