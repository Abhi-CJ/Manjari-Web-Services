from django.db import models


class RoutePage(models.Model):
    """
    Data-driven SEO landing page for a specific route or service.
    Each instance generates a unique URL like /gwalior-to-delhi-cab/
    with its own <title>, meta description, H1, content, and FAQ schema.
    """

    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="URL slug, e.g. 'gwalior-to-delhi-cab'. Becomes the page URL.",
    )
    title = models.CharField(
        max_length=200,
        help_text="HTML <title> tag. Include target keyword. E.g. 'Gwalior to Delhi Cab — ₹3500 One-Way | Manjari Taxi'",
    )
    meta_description = models.TextField(
        max_length=300,
        help_text="SEO meta description (aim for 150-160 characters).",
    )
    h1_heading = models.CharField(
        max_length=200,
        help_text="Main H1 heading on the page.",
    )
    intro_text = models.TextField(
        help_text="2-3 paragraphs of unique content for the hero area. Supports basic HTML.",
    )
    body_text = models.TextField(
        blank=True,
        default="",
        help_text="Additional body content below the hero. Supports basic HTML.",
    )

    # Route stats (optional — shown as highlight cards)
    distance_km = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Distance in kilometers, e.g. 321",
    )
    duration_hours = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="Approximate travel time in hours, e.g. 5.5",
    )
    starting_price = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Starting fare in INR, e.g. 3500",
    )

    # FAQ data for rich snippets
    faq_json = models.JSONField(
        blank=True,
        default=list,
        help_text='List of {"question": "...", "answer": "..."} objects for FAQ schema.',
    )

    # Publishing
    is_published = models.BooleanField(
        default=False,
        help_text="Only published pages are visible on the site.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'core'
        db_table = "core_routepage"
        verbose_name = "Route Page"
        verbose_name_plural = "Route Pages"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self) -> str:
        return f"/{self.slug}/"
