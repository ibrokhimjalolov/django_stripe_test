import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_item_stripe_session(item) -> str:
    res = stripe.checkout.Session.create(
        client_reference_id=item.id,
        success_url="http://localhost:8000/success",
        mode="payment",
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                    "unit_amount": item.price,
                }, 
                "quantity": 1
            }
        ]
    )
    return res["id"]
