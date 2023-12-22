class OrderProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_order(self, order, payment_details):
        if self.payment_gateway.process_payment(payment_details):
            return "주문 성공"
        else:
            return "주문 실패"

class PaymentGateway:
    def process_payment(self, payment_details):
        # 실제 결제 처리 로직 (여기서는 단순화됨)
        return payment_details["amount"] > 0

import unittest

class TestOrderPaymentIntegration(unittest.TestCase):
    def setUp(self):
        payment_gateway = PaymentGateway()
        self.order_processor = OrderProcessor(payment_gateway)

    def test_successful_order_payment(self):
        order = {"item": "책", "quantity": 1}
        payment_details = {"amount": 100}
        result = self.order_processor.process_order(order, payment_details)
        self.assertEqual(result, "주문 성공")

    def test_failed_order_payment_due_to_insufficient_amount(self):
        order = {"item": "책", "quantity": 1}
        payment_details = {"amount": 0}
        result = self.order_processor.process_order(order, payment_details)
        self.assertEqual(result, "주문 실패")

if __name__ == '__main__':
    unittest.main()

