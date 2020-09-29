import sys

import numpy as np
from IPython.core.display import Image

import praw



reddit = praw.Reddit(
    client_id="0wwkjFTMz7c5cw",
    client_secret="Z620M5db_TyPOaayIuFOcrj5Wbo",
    user_agent="boh",
    username="cmencar",
    password="342681z@R3DD17",
)
subreddit = reddit.subreddit("showerthoughts")

# go by timespan - 'hour', 'day', 'week', 'month', 'year', 'all'
# might need to go longer than an hour to get entries...
top_submissions = subreddit.top('hour')

n_sub = int(sys.argv[1]) if len(sys.argv) > 1 else 1

i = 0
while i < n_sub:
    top_submission = next(top_submissions)
    i += 1

top_post = top_submission.title

upvotes = []
downvotes = []
contents = []

for sub in top_submissions:
    try:
        ratio = sub.upvote_ratio
        ups = int(round((ratio*sub.score)/(2*ratio - 1))
                  if ratio != 0.5 else round(sub.score/2))
        upvotes.append(ups)
        downvotes.append(ups - sub.score)
        contents.append(sub.title)
    except Exception as e:
        continue

votes = np.array( [ upvotes, downvotes] ).T
