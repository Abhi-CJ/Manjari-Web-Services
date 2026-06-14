from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from core.forms import ReviewForm
from core.utils.rate_limit import is_rate_limited
from core.services import ReviewService

def submit_review(request: HttpRequest) -> HttpResponse:
    """
    Handles POST submissions for customer reviews.
    Includes cache-based rate-limiting (max 3 reviews per 5 minutes per IP).
    """
    if request.method == "POST":
        # Rate limit: max 3 reviews per 5 minutes per IP
        if is_rate_limited(
            request,
            key_prefix="submit_review",
            limit=3,
            period=300,
            error_message="Too many review submissions. Please try again in a few minutes."
        ):
            return redirect("home")

        form = ReviewForm(request.POST)
        if form.is_valid():
            ReviewService.create_review(form.cleaned_data)
            messages.success(
                request,
                "Thank you! Your review has been submitted for approval."
            )
        else:
            messages.error(
                request,
                "Invalid review data. Please check your inputs and try again."
            )

    return redirect("home")
