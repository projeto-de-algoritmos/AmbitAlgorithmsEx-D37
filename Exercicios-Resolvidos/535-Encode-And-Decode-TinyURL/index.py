class Codec:

    def __init__(self):
        self.url_mapping = {}
        self.counter = 0
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.url_mapping:
            return self.base_url + self.url_mapping[longUrl]
        else:
            self.counter += 1
            short_url = str(self.counter)
            self.url_mapping[longUrl] = short_url
            return self.base_url + short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        short_url = shortUrl[len(self.base_url):]
        for long_url, s_url in self.url_mapping.items():
            if s_url == short_url:
                return long_url