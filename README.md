````markdown
# Reddit Post Scraper (PRAW + JSON)

This Python script collects the top **hot posts** from a specific subreddit (default: `r/python`) using the Reddit API via the `praw` library and stores the structured post data into a JSON file.

## Features

- Fetches up to 400 hot posts from a subreddit.
- Extracts key metadata: title, author, score, number of comments, URL, flair, and more.
- Saves data as a JSON array to `sotred_posts.json`.
- Compatible with Reddit's current API usage policy.

## Requirements

- Python 3.6+
- `praw` library

## Installation

Install required dependencies using pip:

```bash
pip install praw
````

## Setup

1. Create a Reddit App:

   * Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
   * Click "create another app".
   * Set type to "script".
   * Copy the `client_id` and `client_secret`.

2. Update the script:
   Replace the placeholders:

   ```python
   client_id='YOUR_CLIENT_ID'
   client_secret='YOUR_CLIENT_SECRET'
   user_agent='MyRedditScraper'
   ```

## Usage

Run the script:

```bash
python reddit_scraper.py
```

This will generate a `sotred_posts.json` file containing the scraped post data.

## Output Format

Each entry in `sotred_posts.json` is a dictionary with the following structure:

```json
{
    "id": "post_id",
    "title": "Post Title",
    "selftext": "Post body",
    "author": "username",
    "score": 123,
    "upvotes": 130,
    "downvotes": 7,
    "num_comments": 56,
    "created_utc": 1686543210.0,
    "url": "https://...",
    "permalink": "/r/python/comments/...",
    "subreddit": "python",
    "is_self": true,
    "over_18": false,
    "stickied": false,
    "locked": false,
    "flair": "Discussion"
}
```

## License

MIT License

## Disclaimer

Use responsibly. Always respect Reddit's [API terms of use](https://www.redditinc.com/policies/data-api-terms).
