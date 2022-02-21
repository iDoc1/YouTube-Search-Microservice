# Author: Ian Docherty
# Description: Defines a YouTubeApi class that allows the client
#              to run search queries on Google's YouTube API

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


class YouTubeApi:
    """
    This class represents a connection to Google's YouTube
    API and provides methods that allow the client program
    to obtain YouTube serach results
    """

    def __init__(self):
        load_dotenv()
        api_key = os.getenv('YOUTUBE_API_KEY')
        self._youtube_service = build('youtube', 'v3', developerKey=api_key)

    def search(self, search_string, max_results):
        """
        Given a search string, submits a GET request to the YouTube
        API using this string as the search parameter, then returns
        the specified number of results as a list of URLs
        :param search_string: the string to submit a search request for
        :param max_results: the max number of URLs to return
        :return: A list of URLs of the top 3 results
        """

        # Create and execute request
        request = self._youtube_service.search().list(
            part="snippet",
            maxResults=max_results,
            type="videos",
            q=search_string
        )
        response = request.execute()

        # Create URLs and store in a list
        url_list = []
        base_url = "https://www.youtube.com/watch?v="
        for video in response['items']:
            url_list.append(base_url + video['id']['videoId'])

        return url_list


# Test code to print search results for a specified query
if __name__ == "__main__":
    api = YouTubeApi()
    print(api.search("bicep curl", 3))
