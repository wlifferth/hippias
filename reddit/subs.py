import praw
from urllib.request import urlretrieve

def get_post(subreddit_name):
    reddit = praw.Reddit(
        client_id='F9gwgA2NPHDGew',
        client_secret='H-Wd1CdpmFhta5iPBkymjJ1Q4Ko',
        user_agent='macos:hippias:v1.0.0 (by/u/wlifferth)',
        )
    sub = reddit.subreddit('dataisbeautiful')
    print(dir(sub))
    top = sub.top('week', limit=1)
    post = list(top)[0]
    return post.url
