import json
from tests.routes.base import TestBase

class TestProcesses(TestBase):
    def setUp(self):
        pass

    def test_decimal_to_roman(self):
        input_01 = {"decimal": 9, "user_id": 1}
        test_01 = self.client.post('/api/processes/decimal_to_roman/', input_01).data
        output_01 = 1
        self.assertEqual(test_01, output_01)

        input_02 = {"decimal": 7, "user_id": 1}
        test_02 = self.client.post('/api/processes/decimal_to_roman/', input_02).data
        output_02 = 1
        self.assertEqual(test_02, output_02)

        input_03 = {"decimal": 24, "user_id": 1}
        test_03 = self.client.post('/api/processes/decimal_to_roman/', input_03).data
        output_03 = 1
        self.assertEqual(test_03, output_03)

    def test_characters(self):
        input_01 = 1
        test_01 = self.client.get('/api/processes/' + str(input_01) + '/characters/').data
        output_01 = ["X"]
        self.assertEqual(test_01, output_01)