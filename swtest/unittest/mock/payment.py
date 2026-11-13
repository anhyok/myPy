# payment.py

import requests

def process_payment(user_id, amount):
    response = requests.post("http://example.com/api/payments", data={"user_id": user_id, "amount": amount})
    if response.status_code == 200:
        return "결제 성공"
    else:
        return "결제 실패"
