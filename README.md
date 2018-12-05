# RedditWiper
Script to remove user's Reddit post submissions and comments.

Developed with Python Version: 3.6.5


## What it Does

This script will run the *delete_comments* and *delete_submissions* functions as many times as assigned. The script accesses your Reddit account through PRAW and works in reverse chronological order, deleting your most recent posts first.

There is a 2-second delay between each post deletion to accomodate the API's 30 requests per minute restriction. 


## Packages

To run this script, you must install **PRAW** (the Python Reddit API Wrapper - version 5.4.0 used here).

You can find more info, including installation help, on the [PRAW documentation page](https://praw.readthedocs.io/).

Other modules used are packaged with current python version.


##  Running the Script

See the usage guide below. Running the file without any options will go through all of your Reddit comments and submissions and ask you to confirm each deletion.


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
