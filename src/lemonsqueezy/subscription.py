from dataclasses import dataclass
from typing import Optional, Mapping


@dataclass
class Urls:
    update_payment_method: str


@dataclass
class Attributes:
    store_id: int
    customer_id: int
    order_id: int
    order_item_id: int
    product_id: int
    variant_id: int
    product_name: str
    variant_name: str
    user_name: str
    user_email: str
    status: str
    status_formatted: str
    card_brand: str
    card_last_four: str
    pause: Optional[bool]
    cancelled: bool
    trial_ends_at: Optional[str]
    billing_anchor: int
    urls: Urls
    renews_at: str
    ends_at: Optional[str]
    created_at: str
    updated_at: str
    test_mode: bool


@dataclass
class Subscription:
    type: str
    id: str
    attributes: Attributes
    relationships: Optional[Mapping[str, any]]
    links: Optional[Mapping[str, any]]
