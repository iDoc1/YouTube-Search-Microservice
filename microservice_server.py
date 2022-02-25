# Author: Ian Docherty
# Description: Creates an RPyC microservice server with a method that,
#              when called, will return a list of URLs given a search
#              string

import rpyc
from youtube_api import YouTubeApi


class YouTubeService(rpyc.Service):
    """
    Defines a server that provide YouTube search functionality
    """

    def on_connect(self, conn):
        pass

    @staticmethod
    def exposed_youtube_search(search_string, max_results):
        """
        Searches YouTube using a given search string then returns a
        specified number of URLs in a list
        :param search_string: the string to perform YouTube search with
        :param max_results: the max number of results to return
        :return: a list or URL strings
        """

        # Create a YouTube API object and perform search
        youtube_api = YouTubeApi()
        return youtube_api.search(search_string, max_results)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(YouTubeService, port=18861)
    t.start()
