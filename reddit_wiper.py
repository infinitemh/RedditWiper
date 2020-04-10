import datetime
import time

import praw
from args import parser

# Reddit Login parameters. Adjust as necessary.
# client_id and client_secret can be obtained by creating an app entry on Reddit https://www.reddit.com/prefs/apps/
# (When you're there, a script app, and http://localhost:8080 as the redirect uri should suffice.)

USERNAME = ""
PASSWORD = ""
CLIENT_ID = ""
CLIENT_SECRET = ""


class Wiper:
    def __init__(self, username, password, client_id, client_secret):
        self.reddit = praw.Reddit(
            username=username,
            password=password,
            client_id=client_id,
            client_secret=client_secret,
            user_agent=f"localhost:Bot Test:v0.1 (by /u/{username})",
        )

    def delete_comments(self, comment_count=None, no_confirm=False):
        # grab the user's most recent comments up to 'comment_count'
        comments_list = self.reddit.user.me().comments.new(limit=comment_count)
        if comments_list:
            for comment in comments_list:
                print("Comment :", comment.body)
                print("Posted on: ", datetime.datetime.fromtimestamp(int(comment.created)))
                if not no_confirm:
                    self.confirm(comment, "comment")
                else:
                    comment.delete()
                    print("Deleted. \n")
                    # a 2 sec delay between deletion to adhere to Reddit's 30 requests per minute restriction.
                    time.sleep(2)
        else:
            print('There are no comments to delete')
        print("Comments deletion complete.")

    def delete_submissions(self, submissions_count=None, no_confirm=False):
        # grab the user's most recent submissions up to 'submissions_count'
        submissions_list = self.reddit.user.me().submissions.new(
            limit=submissions_count
        )
        if submissions_list:
            for submission in submissions_list:
                print("Submission : ", submission.title)
                print(
                    "Submitted on: ",
                    datetime.datetime.fromtimestamp(int(submission.created)),
                )
                if not no_confirm:
                    self.confirm(submission, "submission")
                else:
                    submission.delete()
                    print("Deleted. \n")
                    # a 2 sec delay between deletion to adhere to Reddit's 30 requests per minute restriction.
                    time.sleep(2)
        else:
            print('There are no submissions to delete')
        print("Submissions deletion complete.")

    def confirm(self, post, post_type):
        confirm_deletion = input(f"Would you like to delete this {post_type}? Y/N: ")
        if confirm_deletion.upper() == "Y":
            print(f"Deleting {post_type}... \n")
            post.delete()
            # a 2 sec delay between deletion to adhere to Reddit's 30 requests per minute restriction.
            time.sleep(2)
        elif confirm_deletion.upper() == "N":
            print(f"{post_type} saved. \n")
            time.sleep(2)
            pass
        else:
            print("Input value error. Please enter (Y/N): \n")
            self.confirm(post, post_type)


if __name__ == "__main__":
    # confirm all credentials are found, else throw an error.
    for field, required_value in {
        "username": USERNAME,
        "password": PASSWORD,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }.items():
        if not required_value:
            raise Exception(f"Please enter {field} information inside reddit_wiper.py")
    # get command line options inputted by user
    options = vars(parser.parse_args())
    wiper = Wiper(USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET)
    if options["delete_e"]:  # delete everything
        print("Deleting all comments:")
        wiper.delete_comments(comment_count=None, no_confirm=options["no_confirm"])
        print("Deleting all submissions:")
        wiper.delete_submissions(
            submissions_count=None, no_confirm=options["no_confirm"]
        )
    else:
        if not options["number_of_comments"] == 0:
            print("Deleting comments: ")
            wiper.delete_comments(
                comment_count=options["number_of_comments"],
                no_confirm=options["no_confirm"],
            )
        elif not options["number_of_submissions"] == 0:
            print("Deleting submissions: ")
            wiper.delete_submissions(
                submissions_count=options["number_of_submissions"],
                no_confirm=options["no_confirm"],
            )

    print("Script Completed \n")
