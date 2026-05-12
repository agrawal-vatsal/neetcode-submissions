from collections import defaultdict

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.tweet_count + 1))
        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_to_handle = []
        users_to_check = self.followers[userId]
        users_to_check.add(userId)
        for follower in users_to_check:
            tweets_to_handle.extend(self.tweets[follower])

        tweets_to_handle.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in tweets_to_handle[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
