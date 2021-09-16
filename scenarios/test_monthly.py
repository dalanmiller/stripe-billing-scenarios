import pytest


@pytest.fixture
def stripe():
  import stripe
  stripe.api_key = \
    "sk_test_51JaKYiLOi6OCbWGVcbmRgCvTXnYbpdRIdcnYTySuISMHvXst0EqxaagnxTdt6mKtnYORLYFwbWYjWEYyetjqRd090013lfr37f"
  return stripe


def test_monthly_billing_scenario(stripe):

  c = stripe.Customer.create(
    payment_method="pm_card_au"
  )

  pm = stripe.PaymentMethod.list(
    customer=c,
    type="card"
  )['data'][0]

  s = stripe.Subscription.create(
    customer=c,
    default_payment_method=pm,
    items=[{
      "price_data": {
        "product": "prod_KEoJP6yDtsVqqP",
        "recurring": {
          "interval": "month"
        },
        "unit_amount": 1000,
        "currency": "aud",
      }
    }],
  )
  assert s
