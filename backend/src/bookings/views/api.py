from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from core.utils.rate_limit import is_rate_limited
from bookings.forms import BookingForm
from bookings.services import BookingService

def create_booking(request: HttpRequest) -> HttpResponse:
    """
    Handles POST submissions for creating a booking request.
    Includes cache-based rate-limiting (max 3 bookings per 5 minutes per IP).
    """
    if request.method == "POST":
        # Rate limit: max 3 bookings per 5 minutes per IP
        if is_rate_limited(
            request,
            key_prefix="create_booking",
            limit=3,
            period=300,
            error_message="Too many booking requests. Please try again in a few minutes."
        ):
            return redirect("home")

        form = BookingForm(request.POST)
        if form.is_valid():
            BookingService.create_booking(form.cleaned_data)
            messages.success(
                request,
                "Your booking request was submitted successfully. We will contact you soon."
            )
        else:
            messages.error(
                request,
                "Booking request could not be submitted. Please check your details and try again."
            )

    return redirect("home")
