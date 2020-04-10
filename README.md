# RedditWiper
Script to remove user's Reddit post submissions and comments.

## Installation

This script requires **Python > 3.6** and  **PRAW**.

Once [Python > 3.6](https://www.python.org/) is installed and [virtual environment activated](https://docs.python.org/3/library/venv.html),

    pip install praw
    
or

    pip install -r requirements.txt

Edit *reddit_wiper.py* to include the following credentials:

    USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET

client_id and client_secret can be obtained by creating an app entry on reddit: https://www.reddit.com/prefs/apps/

(When you're there, a script app, and http://localhost:8080 as the redirect uri should suffice.)




##  Running the Script

See the usage guide below (python reddit_wiper.py --help). Running the file without any options will go through all of your Reddit comments and submissions and ask you to confirm each deletion.


    usage: RedditWiper.py [-h] [-n] [-e] [-c NUMBER_OF_COMMENTS | -C] [-s NUMBER_OF_SUBMISSIONS | -S]
    A script to delete your Reddit history.
    optional arguments:
 
    -h, --help
    show this help message and exit
    -n, --noconfirm
    Delete without confirming. Confirmation is on by default.
    -e, -E, --everything  
    Delete everything. Other deletion options take precedence.
    -c NUMBER_OF_COMMENTS, --comments NUMBER_OF_COMMENTS
    Delete comments. Default is 0.
    -C, --all-comments
    Delete all comments.
    -s NUMBER_OF_SUBMISSIONS, --submissions NUMBER_OF_SUBMISSIONS, --posts NUMBER_OF_SUBMISSIONS
    Delete submissions. Default is 0
    -S, -P, --all-submissions, --all-posts
    Delete all submissions.
