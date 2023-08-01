import httpx

from lemonsqueezy.page import PageResponse
from lemonsqueezy.subscription import Subscription

LEMONSQUEEZY_API_V1 = "https://api.lemonsqueezy.com/v1"


class LemonSqueezy:

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.http_header = {
            "Authorization": f"Bearer {api_key}"
        }

    def get_all_subscriptions(self) -> PageResponse[Subscription]:
        res = httpx.get(f"{LEMONSQUEEZY_API_V1}/subscriptions", headers=self.http_header)
        res.raise_for_status()
        data: PageResponse[Subscription] = res.json()
        return data
