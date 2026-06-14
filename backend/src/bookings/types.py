from typing import TypedDict, Optional

class BookingFormData(TypedDict):
    name: str
    phone: str
    pickup_location: str
    drop_location: str
    service_type: str
    message: Optional[str]
