import datetime
import calendar


def test_yearly_billing_scenario(customer, stripe_client):
    stripe = stripe_client

    payment_method = stripe.PaymentMethod.list(customer=customer, type="card")["data"][
        0
    ]

    subscription = stripe.Subscription.create(
        customer=customer,
        default_payment_method=payment_method,
        items=[
            {
                "price_data": {
                    "product": "prod_KEoJP6yDtsVqqP",
                    "recurring": {"interval": "year"},
                    "unit_amount": 1000,
                    "currency": "aud",
                }
            }
        ],
    )

    assert subscription

    now = datetime.datetime.now()
    day_next_year = datetime.datetime(
        year=now.year + 1,
        month=now.month,
        day=now.day,
        hour=now.hour,
        minute=now.minute,
        second=now.second,
    )
    day_next_year = day_next_year + datetime.timedelta(seconds=30)
    subscription_end = datetime.datetime.fromtimestamp(subscription.current_period_end)

    assert subscription_end < day_next_year


def test_monthly_billing_scenario(customer, stripe_client):
    stripe = stripe_client

    payment_method = stripe.PaymentMethod.list(customer=customer, type="card")["data"][
        0
    ]

    subscription = stripe.Subscription.create(
        customer=customer,
        default_payment_method=payment_method,
        items=[
            {
                "price_data": {
                    "product": "prod_KEoJP6yDtsVqqP",
                    "recurring": {"interval": "month"},
                    "unit_amount": 1000,
                    "currency": "aud",
                }
            }
        ],
    )

    assert subscription

    now = datetime.datetime.now()
    month_range_start, month_range_end = calendar.monthrange(now.year, now.month)
    day_next_month = datetime.datetime(
        year=now.year,
        month=12 if now.month == 12 else (now.month + 1) % 12,
        day=now.day + 1
        if month_range_start <= now.day + 1 <= month_range_end
        else month_range_end,
    )
    subscription_end = datetime.datetime.fromtimestamp(subscription.current_period_end)

    assert subscription_end < day_next_month


def test_weekly_billing_scenario(customer, stripe_client):
    stripe = stripe_client

    payment_method = stripe.PaymentMethod.list(customer=customer, type="card")["data"][
        0
    ]

    subscription = stripe.Subscription.create(
        customer=customer,
        default_payment_method=payment_method,
        items=[
            {
                "price_data": {
                    "product": "prod_KEoJP6yDtsVqqP",
                    "recurring": {"interval": "week"},
                    "unit_amount": 1000,
                    "currency": "aud",
                }
            }
        ],
    )

    assert subscription

    now = datetime.datetime.now()
    subscription_end = datetime.datetime.fromtimestamp(subscription.current_period_end)

    assert subscription_end < now + datetime.timedelta(weeks=1)


def test_daily_billing_scenario(customer, stripe_client):
    stripe = stripe_client

    payment_method = stripe.PaymentMethod.list(customer=customer, type="card")["data"][
        0
    ]

    subscription = stripe.Subscription.create(
        customer=customer,
        default_payment_method=payment_method,
        items=[
            {
                "price_data": {
                    "product": "prod_KEoJP6yDtsVqqP",
                    "recurring": {"interval": "day"},
                    "unit_amount": 1000,
                    "currency": "aud",
                }
            }
        ],
    )

    assert subscription

    now = datetime.datetime.now()
    subscription_end = datetime.datetime.fromtimestamp(subscription.current_period_end)

    assert subscription_end < now + datetime.timedelta(days=1)
