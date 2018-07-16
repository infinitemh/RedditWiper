# Script to delete your Reddit submission/comment history.

import praw
import time
import datetime

# Login parameters. Adjust as necessary.
# client_id and client_secret can be obtained by creating an app entry in https://www.reddit.com/prefs/apps/
# (When you're there, a script app, and http://localhost:8080 as the redirect uri should suffice.)

username = ""
password = ""
client_id = ""
client_secret = ""


# Login function. Creates a Reddit instance.
def bot_login():
    login = praw.Reddit(username=username,
                    password=password,
                    client_id=client_id,
                    client_secret=client_secret,
                    user_agent='localhost:Bot Test:v0.1 (by /u/InfiniteMH)',)
    return login


reddit_instance = bot_login()

# Confirmation Mode:
# If you would like to run the script in Confirmation Mode, modify the conf_mode variable to "on" (case sensitive).
# Make sure to use quotation marks around the variable to store it as a string value.

conf_mode = ""

def delete_comments(count=None):
    if conf_mode == 'on':
        comments_listobj = reddit_instance.user.me().comments.new(limit=count)
        for comment in comments_listobj:
            print('Comment :', comment.body)
            print('Posted on: ', datetime.datetime.fromtimestamp(int(comment.created)))
            print('Would you like to delete this comment? Y/N: ')
            comment_confirmation = input()
            if comment_confirmation.upper() == 'Y':
                comment.delete()
                print('Deleted. \n')
                # time.sleep(2) - a 2 sec delay between deletion because of Reddit's 30 requests per minute restriction.
                time.sleep(2)
            elif comment_confirmation.upper() == 'N':
                print('Comment not deleted. \n')
                time.sleep(2)
                pass
            else:
                print('Input value error. Comment not deleted. \n')
                time.sleep(2)
                pass
    else:
        comments_listobj = reddit_instance.user.me().comments.new(limit=count)
        for comment in comments_listobj:
            print('Deleting :', comment.body)
            print('Posted on: ', datetime.datetime.fromtimestamp(int(comment.created)))
            comment.delete()
            print('Deleted. \n')
            time.sleep(2)

def delete_submissions(count=None):
    if conf_mode == 'on':
        submissions_listobj = reddit_instance.user.me().submissions.new(limit=count)
        for submission in submissions_listobj:
            print('Submission : ', submission.title)
            print('Submitted on: ', datetime.datetime.fromtimestamp(int(submission.created)))
            print('Would you like to delete this submission? Y/N: ')
            post_confirmation = input()
            if post_confirmation.upper() == 'Y':
                submission.delete()
                print('Deleted. \n')
                time.sleep(2)
            elif post_confirmation.upper() == 'N':
                print('Submission not deleted. \n')
                time.sleep(2)
                pass
            else:
                print('Input value error. Submission not deleted. \n')
                time.sleep(2)
                pass
    else:
        submissions_listobj = reddit_instance.user.me().submissions.new(limit=count)
        for submission in submissions_listobj:
            print('Deleting : ', submission.title)
            print('Submitted on: ', datetime.datetime.fromtimestamp(int(submission.created)))
            submission.delete()
            print('Deleted. \n')
            time.sleep(2)

# Run the function you wish to run with the desired number of posts/comments.
# Nothing between the parentheses will delete ALL of that type.
delete_comments(0)
delete_submissions(0)

print('Script Completed \n')
