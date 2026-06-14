import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.decorators.cache import cache_page

from core.models import Service, Vehicle, Review, RoutePage
from bookings.forms import BookingForm
from core.forms import ReviewForm

def home(request: HttpRequest) -> HttpResponse:
    """
    Home page view displaying services, fleet, approved reviews, and forms.
    Uses database optimization via only() to load required fields.
    """
    approved_reviews = (
        Review.objects.filter(approved=True)
        .only("id", "customer_name", "location", "review", "rating", "created_at")
        .order_by("-created_at")
    )

    # Fetch published route pages for internal linking
    route_pages = (
        RoutePage.objects.filter(is_published=True)
        .only("slug", "h1_heading")
        .order_by("h1_heading")
    )

    context = {
        "services": Service.objects.only("id", "title", "description"),
        "vehicles": Vehicle.objects.only(
            "id", "name", "category", "image", "seats", "features"
        ),
        "reviews": approved_reviews,
        "form": BookingForm(),
        "review_form": ReviewForm(),
        "route_pages": route_pages,
    }

    return render(request, "home.html", context)


def route_page(request: HttpRequest, slug: str) -> HttpResponse:
    """
    Dedicated SEO landing page for a specific route or service.
    Each page has its own title, meta description, H1, content, and FAQ schema.
    """
    page = get_object_or_404(RoutePage, slug=slug, is_published=True)

    # Prepare FAQ schema JSON for the template
    faq_schema = ""
    if page.faq_json:
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq["question"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq["answer"],
                    },
                }
                for faq in page.faq_json
            ],
        }
        faq_schema = json.dumps(schema, ensure_ascii=False)

    context = {
        "page": page,
        "form": BookingForm(),
        "faq_schema": faq_schema,
    }

    return render(request, "route_page.html", context)


@cache_page(86400, cache='default')
def robots_txt(request: HttpRequest) -> HttpResponse:
    """
    Serves the robots.txt file, cached for 24 hours.
    """
    return render(request, "robots.txt", content_type="text/plain")

