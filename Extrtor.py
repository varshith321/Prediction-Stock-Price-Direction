import praw


reddit = praw.Reddit(client_id='YBmTOHqk0L14mg',
                    client_secret='qdYllIZqF5yjfWf464N2_HcuLwk',
                    password='password',
                    user_agent='Test script',
                    username='AgoResolution')

print(reddit.user.me())

reddit.read_only = True

Apple_sub = reddit.subreddit('Apple')
for submission in Apple_sub.stream.submissions():
	print(submission.title)