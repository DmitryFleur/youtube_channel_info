from django.http import JsonResponse
from django.views import View

from youtube_channel.data_processors.channel_processor import ChannelProcessor


class ChannelInfo(View):

    def get(self, request):
        channel_id = 'UCgFvT6pUq9HLOvKBYERzXSQ'
        channel = ChannelProcessor(channel_id)
        res = {
            'data': None,
            'ok': False
        }

        try:
            channel_data = channel.process()
        except Exception:
            return JsonResponse(res)
        else:
            res['data'] = channel_data
            res['ok'] = True
            return JsonResponse(res)
