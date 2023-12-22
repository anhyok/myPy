# test_payment.py

import unittest
from unittest.mock import patch
from payment import process_payment

class TestPayment(unittest.TestCase):
    @patch('payment.requests.post')
    def test_process_payment_success(self, mock_post):
        # 모의 응답 설정
        mock_post.return_value.status_code = 200

        # 함수 호출 및 결과 검증
        response = process_payment("user123", 100)
        self.assertEqual(response, "결제 성공")

    @patch('payment.requests.post')
    def test_process_payment_failure(self, mock_post):
        # 모의 응답 설정
        mock_post.return_value.status_code = 400

        # 함수 호출 및 결과 검증
        response = process_payment("user123", 100)
        self.assertEqual(response, "결제 실패")

if __name__ == '__main__':
    unittest.main()
