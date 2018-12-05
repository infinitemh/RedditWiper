# Script to delete your Reddit submission/comment history.

import argparse
import datetime
import time
import praw

parser = argparse.ArgumentParser(description="A script to delete your Reddit history.")
parser.add_argument('-n', '--noconfirm', dest='no_conf_mode', action='store_true', default=False,
                    help='Delete without confirming. Confirmation is on by default.')
parser.add_argument('-e', '-E', '--everything', dest='delete_e', action='store_true', default=True,
                    help='Delete everything. Other deletion options take precedence for safety.')

comment_group = parser.add_mutually_exclusive_group()
comment_group.add_argument('-c', '--comments', dest='number_of_comments', action='store', default=0, type=int,
                           help='Delete comments. Default is 0.')
comment_group.add_argument('-C', '--all-comments', dest='number_of_comments', action='store_const', const=None,
                           default=0,
                           help='Delete all comments.')

submissions_group = parser.add_mutually_exclusive_group()
submissions_group.add_argument('-s', '--submissions', '--posts', dest='number_of_submissions', action='store', type=int,
                               default=0, help='Delete submissions. Default is 0')
submissions_group.add_argument('-S', '-P', '--all-submissions', '--all-posts', dest='number_of_submissions',
                               action='store_const', const=None, default=0,
                               help='Delete all submissions.')

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
                        user_agent='localhost:Bot Test:v0.1 (by /u/InfiniteMH)', )
    return login


reddit_instance = bot_login()


def delete_comments(count=None, no_conf_mode=False):
    comments_listobj = reddit_instance.user.me().comments.new(limit=count)
    for comment in comments_listobj:
        print('Comment :', comment.body)
        print('Posted on: ', datetime.datetime.fromtimestamp(int(comment.created)))
        if not no_conf_mode:
            comment_confirmation = input('Would you like to delete this comment? Y/N: ')
            if comment_confirmation.upper() == 'Y':
                print('Deleting... \n')
                comment.delete()
                time.sleep(2)
                # time.sleep(2) - a 2 sec delay between deletion because of Reddit's 30 requests per minute restriction.
            elif comment_confirmation.upper() == 'N':
                print('Comment saved. \n')
                time.sleep(2)
                pass
            else:
                print('Input value error. Please enter Y/N: \n')
                time.sleep(2)
                continue
        else:
            comment.delete()
            print('Deleted. \n')
            time.sleep(2)
    print('Comments deletion complete.')


def delete_submissions(count=None, no_conf_mode=False):
    submissions_listobj = reddit_instance.user.me().submissions.new(limit=count)
    for submission in submissions_listobj:
        print('Submission : ', submission.title)
        print('Submitted on: ', datetime.datetime.fromtimestamp(int(submission.created)))
        if not no_conf_mode:
            post_confirmation = input('Would you like to delete this submission? Y/N: ')
            if post_confirmation.upper() == 'Y':
                print('Deleting.. \n')
                submission.delete()
                time.sleep(2)
            elif post_confirmation.upper() == 'N':
                print('Submission saved. \n')
                time.sleep(2)
                pass
            else:
                print('Input value error. Please enter Y/N. \n')
                time.sleep(2)
                continue
        else:
            submission.delete()
            print('Deleted. \n')
            time.sleep(2)
    print('Submissions deletion complete.')


# usage: RedditWiper.py [-h] [-n] [-e] [-c NUMBER_OF_COMMENTS | -C]
#                      [-s NUMBER_OF_SUBMISSIONS | -S]
# A script to delete your Reddit history.
# optional arguments:
#   -h, --help            show this help message and exit
#   -n, --noconfirm       Delete without confirming. Confirmation is on by
#                         default.
#   -e, -E, --everything  Delete everything. Other deletion options take precedence for safety.
#   -c NUMBER_OF_COMMENTS, --comments NUMBER_OF_COMMENTS
#                         Delete comments. Default is 0.
#   -C, --all-comments    Delete all comments.
#   -s NUMBER_OF_SUBMISSIONS, --submissions NUMBER_OF_SUBMISSIONS, --posts NUMBER_OF_SUBMISSIONS
#                         Delete submissions. Default is 0
#   -S, -P, --all-submissions, --all-posts
#                         Delete all submissions. -c/-p takes precedence for
#                         safety.
                                         
if __name__ == "__main__":
    options = vars(parser.parse_args())
    if options['delete_e'] and options['number_of_comments'] == 0 and options['number_of_submissions'] == 0:
        print('Deleting all comments:')
        delete_comments(count=None, no_conf_mode=options['no_conf_mode'])
        print('Deleting all submissions:')
        delete_submissions(count=None, no_conf_mode=options['no_conf_mode'])
    else:
        if not options['number_of_comments'] == 0:
            print("Deleting comments: ")
            delete_comments(count=options['number_of_comments'], no_conf_mode=options['no_conf_mode'])
        elif not options['number_of_submissions'] == 0:
            print("Deleting submissions: ")
            delete_submissions(count=options['number_of_submissions'], no_conf_mode=options['no_conf_mode'])

    print('Script Completed \n')
