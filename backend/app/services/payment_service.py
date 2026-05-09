from typing import List
from ..models.payment import Payment

class PaymentService:
    def __init__(self):
        self._payments: List[Payment] = []
        self._next_id = 1

    async def process_payment(self, payment: Payment) -> Payment:
        payment.id = self._next_id
        self._next_id += 1
        self._payments.append(payment)
        return payment
