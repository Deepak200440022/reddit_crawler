import praw
import json

reddit = praw.Reddit(
    client_id='YOUR_CLIENT_iD',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='MyRedditScraper'
)

subreddit = reddit.subreddit('python')
posts = []
for post in subreddit.hot(limit=400):
    post_data = {
        'id': post.id,
        'title': post.title,
        'selftext': post.selftext,
        'author': str(post.author),
        'score': post.score,
        'upvotes': post.ups,
        'downvotes': post.downs,
        'num_comments': post.num_comments,
        'created_utc': post.created_utc,
        'url': post.url,
        'permalink': post.permalink,
        'subreddit': str(post.subreddit),
        'is_self': post.is_self,
        'over_18': post.over_18,
        'stickied': post.stickied,
        'locked': post.locked,
        'flair': post.link_flair_text
    }
    posts.append(post_data)

with open("sotred_posts.json","w", encoding="utf-8") as f:
    json.dump(posts, f, indent = 4, ensure_ascii=False)
print("saved successfully")