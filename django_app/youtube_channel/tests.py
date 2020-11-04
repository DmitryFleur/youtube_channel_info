import json

from django.test import TestCase


class TestChannelInfo(TestCase):

    def test_happy_flow(self):
        req = self.client.get('/channel_info/')
        res = json.loads(req.content)

        self.assertEqual(res['data']['channel_name'], 'Davie504')
        self.assertEqual(res['data']['total_views'], 1266904712)
        self.assertEqual(res['data']['avg_num_of_views'], 2107994.5291181365)
        self.assertTrue(res['ok'])
