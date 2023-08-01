import unittest
from unittest.mock import MagicMock
from lemonsqueezy.client import LemonSqueezy
from lemonsqueezy.page import PageResponse
from lemonsqueezy.subscription import Subscription


class TestLemonSqueezy(unittest.TestCase):
    def setUp(self):
        # Create an instance of YourClass and set the necessary attributes, if any
        self.client = LemonSqueezy(api_key="fake-api-key")

    def test_get_all_subscriptions(self):
        # Mock the httpx.get method to return a predefined JSON response
        mock_response = {
            "meta": {
                "page": {
                    "currentPage": 1,
                    "from": 1,
                    "lastPage": 1,
                    "perPage": 10,
                    "to": 10,
                    "total": 10
                }
            },
            "jsonapi": {
                "version": "1.0"
            },
            "links": {
                "first": "https://api.lemonsqueezy.com/v1/subscriptions?page%5Bnumber%5D=1&page%5Bsize%5D=10&sort=-createdAt",
                "last": "https://api.lemonsqueezy.com/v1/subscriptions?page%5Bnumber%5D=1&page%5Bsize%5D=10&sort=-createdAt"
            },
            "data": [
                {
                    "type": "subscriptions",
                    "id": "1",
                    "attributes": {
                        "store_id": 1,
                        "customer_id": 1,
                        "order_id": 1,
                        "order_item_id": 1,
                        "product_id": 1,
                        "variant_id": 1,
                        "product_name": "Example Product",
                        "variant_name": "Example Variant",
                        "user_name": "Darlene Daugherty",
                        "user_email": "gernser@yahoo.com",
                        "status": "active",
                        "status_formatted": "Active",
                        "card_brand": "visa",
                        "card_last_four": "42424",
                        "pause": None,
                        "cancelled": False,
                        "trial_ends_at": None,
                        "billing_anchor": 12,
                        "urls": {
                            "update_payment_method": "https://my-store.lemonsqueezy.com/my-orders/2ba92a4e-a00a-45d2-a128-16856ffa8cdf/subscription/8/update-payment-method?expires=1666869343&signature=9985e3bf9007840aeb3951412be475abc17439c449c1af3e56e08e45e1345413"
                        },
                        "renews_at": "2022-11-12T00:00:00.000000Z",
                        "ends_at": None,
                        "created_at": "2021-08-11T13:47:27.000000Z",
                        "updated_at": "2021-08-11T13:54:19.000000Z",
                        "test_mode": False
                    },
                    "relationships": {
                        "store": {
                            "links": {
                                "related": "https://api.lemonsqueezy.com/v1/subscriptions/1/store",
                                "self": "https://api.lemonsqueezy.com/v1/subscriptions/1/relationships/store"
                            }
                        },
                        "customer": {
                            "links": {
                                "related": "https://api.lemonsqueezy.com/v1/subscriptions/1/customer",
                                "self": "https://api.lemonsqueezy.com/v1/subscriptions/1/relationships/customer"
                            }
                        },
                        "order": {
                            "links": {
                                "related": "https://api.lemonsqueezy.com/v1/subscriptions/1/order",
                                "self": "https://api.lemonsqueezy.com/v1/subscriptions/1/relationships/order"
                            }
                        },
                        "order-item": {
                            "links": {
                                "related": "https://api.lemonsqueezy.com/v1/subscriptions/1/order-item",
                                "self": "https://api.lemonsqueezy.com/v1/subscriptions/1/relationships/order-item"
                            }
                        },
                        "product": {
                            "links": {
                                "related": "https://api.lemonsqueezy.com/v1/subscriptions/1/product",
                                "self": "https://api.lemonsqueezy.com/v1/subscriptions/1/relationships/product"
                            }
                        },
                        "variant": {
                            "links": {
                                "related": "https://api.lemonsqueezy.com/v1/subscriptions/1/variant",
                                "self": "https://api.lemonsqueezy.com/v1/subscriptions/1/relationships/variant"
                            }
                        },
                        "subscription-invoices": {
                            "links": {
                                "related": "https://api.lemonsqueezy.com/v1/subscriptions/1/subscription-invoices",
                                "self": "https://api.lemonsqueezy.com/v1/subscriptions/1/relationships/subscription-invoices"
                            }
                        }
                    },
                    "links": {
                        "self": "https://api.lemonsqueezy.com/v1/subscriptions/1"
                    }
                }
            ]
        }

        # Mock httpx.get to return the predefined response
        with unittest.mock.patch('httpx.get') as mock_get:
            mock_get.return_value = MagicMock()
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response

            # Call the function and get the result
            result = self.client.get_all_subscriptions()

            # Assertions
            self.assertIsInstance(result, PageResponse)
            self.assertIsInstance(result.data, list)
            self.assertEqual(len(result.data), 1)
            self.assertIsInstance(result.data[0], Subscription)
            # Add more assertions based on the actual data you expect


if __name__ == '__main__':
    unittest.main()
