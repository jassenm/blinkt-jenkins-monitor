class FeedSource:

    def get_feed_data(self):
        return ""


class JenkinsFeedSource(FeedSource):

    def __init__(self, baseUrl=None):
        self.baseUrl = baseUrl

    def get_feed_data(self):
        import urllib3
        pool = urllib3.PoolManager()
        response = pool.request('GET', self.baseUrl + "/rssLatest")
        return response.data


class TestFeedSource(FeedSource):

    def __init__(self, src=None):
        self.src = src

    def get_feed_data(self):
        return self.src
