import json
from rest_framework.test import APITestCase


class TestBase(APITestCase):

    def setUp(self):
        pass

    def assertJson(self, json_a, json_b):
        self.assertEqual(json.dumps(json_a, indent=2, sort_keys=True),
                         json.dumps(json_b, indent=2, sort_keys=True))