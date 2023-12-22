# test_weather.py

import unittest
from unittest.mock import patch
from weather import get_weather

class TestWeather(unittest.TestCase):
    @patch('weather.requests.get')
    def test_get_weather(self, mock_get):
        # 예상되는 응답을 설정합니다.
        example_api_response = {
            'location': 'Seoul',
            'temperature': '10',
            'description': 'Sunny'
        }
        mock_get.return_value.json.return_value = example_api_response

        # 함수를 호출하고 결과를 확인합니다.
        response = get_weather("http://example.com/api", "Seoul")
        self.assertEqual(response, example_api_response)

if __name__ == '__main__':
    unittest.main()
