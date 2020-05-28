import logging
from typing import Union
from urllib.parse import urljoin

log = logging.getLogger(__name__)


def refund_payment(
    self,
    order_id: Union[str, int],
    amount: float = None,
    reason: str = None
) -> dict:
    """
    https://developer.paddle.com/api-reference/product-api/payments/refundpayment
    """
    url = urljoin(self.vendors_v2, 'payment/refund')

    json = {
        'order_id': order_id,
        'amount': amount,
        'reason': reason,
    }
    return self.post(url=url, json=json)
