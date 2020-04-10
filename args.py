import argparse

# Command line arguments configuration
parser = argparse.ArgumentParser(description="A script to delete your Reddit history.")
parser.add_argument(
    "-n",
    "--noconfirm",
    dest="no_confirm",
    action="store_true",
    default=False,
    help="Delete without confirming. Confirmation is on by default.",
)
parser.add_argument(
    "-e",
    "-E",
    "--everything",
    dest="delete_e",
    action="store_true",
    default=None,
    help="Delete all posts and comments. ",
)

comment_group = parser.add_mutually_exclusive_group()
comment_group.add_argument(
    "-c",
    "--comments",
    dest="number_of_comments",
    action="store",
    default=0,
    type=int,
    help="Delete comments. Default is 0.",
)
comment_group.add_argument(
    "-C",
    "--all-comments",
    dest="number_of_comments",
    action="store_const",
    const=None,
    default=0,
    help="Delete all comments.",
)

submissions_group = parser.add_mutually_exclusive_group()
submissions_group.add_argument(
    "-s",
    "--submissions",
    "--posts",
    dest="number_of_submissions",
    action="store",
    default=0,
    type=int,
    help="Delete submissions. Default is 0",
)
submissions_group.add_argument(
    "-S",
    "-P",
    "--all-submissions",
    "--all-posts",
    dest="number_of_submissions",
    action="store_const",
    const=None,
    default=0,
    help="Delete all submissions.",
)
