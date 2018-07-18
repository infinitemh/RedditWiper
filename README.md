# RedditWiper
Script to remove user's Reddit post submissions and comments.

Developed with Python Version: 3.6.5


## Packages

To run this script, you must install **PRAW** (the Python Reddit API Wrapper - version 5.4.0 used here).

You can find more info, including installation help, on the [PRAW documentation page](https://praw.readthedocs.io/).

Other modules used are packaged with current python version.


##  Running the Script

In order to run RedditWiper.py, you must modify variables in the python script file. Instructions on modifying these variables can be found in the file itself.


## What it Does

This script will run the *delete_comments* and *delete_submissions* functions as many times as assigned. The script accesses your Reddit account through PRAW and works in reverse chronological order, deleting your most recent posts first.

The **DEFAULT** mode is automatic. You can enable **CONFIRMATION MODE** which will ask for a yes/no confirmation input before deleting each post.

Because of Reddit's request limit, there is a 2-second delay between each post deletion. As such, the script is limited in the number of times it can delete posts before it is restricted.
Thus, in the script's current state, there is no way to delete EVERY post at once. If the script completes without deleting everything, simply run the script again until all posts
have been deleted.

The script will stop when it has run out of posts. However, you will find that you can continue to run the script even when your account has no posts of either type. Plans to change this behavior may come in future updates, but for now we are leaving it as is.





