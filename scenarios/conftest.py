import pytest
import stripe


@pytest.fixture
def stripe_client():
    stripe.api_key = "sk_test_51JaKYiLOi6OCbWGVcbmRgCvTXnYbpdRIdcnYTySuISMHvXst0EqxaagnxTdt6mKtnYORLYFwbWYjWEYyetjqRd090013lfr37f"

    return stripe


@pytest.fixture
def customer(stripe_client):
    return stripe_client.Customer.create(payment_method="pm_card_au")
