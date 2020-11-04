import requests
import json
from django_app.settings import YOUTUBE_API_KEY


class ChannelProcessor:
    """
    Get and process channel's data using Youtube api

    Parameters:
        channel_id (str): id of desired channel

    Returns:
        dict: aggregated data
    """
    def __init__(self, channel_id: str):
        self.channel_id = channel_id

    def _get_channel_data(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={self.channel_id}&fields=items(contentDetails%2Cid%2Csnippet(country%2Cdescription%2Ctitle)%2Cstatistics%2Cstatus)%2CnextPageToken%2CpageInfo%2CprevPageToken%2CtokenPagination&key={YOUTUBE_API_KEY}'
        res = requests.get(url)
        if res.status_code == 200:
            data = json.loads(res.content)['items'][0]
            self._validate_data(data)
            return data

        raise Exception('Something went wrong during youtube api request')

    @staticmethod
    def _validate_data(data):
        required_keys = ['viewCount', 'videoCount']
        msg = 'Not valid data. Check response from youtube'
        if 'statistics' not in data:
            raise Exception(msg)

        for key in required_keys:
            if key not in data['statistics']:
                raise Exception(msg)

        if 'snippet' not in data and 'title' not in data['snippet']:
            raise Exception(msg)

    @staticmethod
    def _get_number_of_views(data):
        return int(data['statistics']['viewCount'])

    @staticmethod
    def _get_video_count(data):
        return int(data['statistics']['videoCount'])

    @staticmethod
    def _calc_avg_number_of_views(total_views, video_count):
        return total_views / video_count

    @staticmethod
    def _get_channel_name(data):
        return data['snippet']['title']

    def process(self):
        channel_data = self._get_channel_data()
        total_views = self._get_number_of_views(channel_data)
        video_count = self._get_video_count(channel_data)
        res = {
            'channel_name': self._get_channel_name(channel_data),
            'total_views': total_views,
            'avg_num_of_views':
                self._calc_avg_number_of_views(total_views, video_count)
        }
        return res
