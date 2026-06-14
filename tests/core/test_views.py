from django.test import TestCase
from django.urls import reverse


class HomepagePerformanceTests(TestCase):
    """
    Test suite for homepage rendering, scripts, styling, and accessibility landmarks.
    """
    def test_homepage_renders_the_main_script_without_template_errors(self) -> None:
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "static/js/main.min.js")
        self.assertContains(response, "preconnect")
        self.assertContains(response, "main.min.js")
        self.assertContains(response, 'width="380"')
        self.assertContains(response, 'height="160"')
        self.assertNotContains(response, "{%")

    def test_homepage_includes_accessibility_improvements(self) -> None:
        response = self.client.get(reverse("home"))

        # Navigation accessibility
        self.assertContains(response, 'aria-label="Toggle navigation menu"')
        self.assertContains(response, 'aria-expanded="false"')
        self.assertContains(response, 'id="primary-navigation"')

        # Dynamic contact info rendered from context processor
        self.assertContains(response, 'tel:+919399623699')
        self.assertContains(response, 'https://wa.me/919399623699')

        # Floating CTA accessibility
        self.assertContains(response, 'aria-label="Contact us on WhatsApp"')
        self.assertContains(response, 'aria-label="Call Manjari Taxi now"')

        # Section headings for screen readers
        self.assertContains(response, 'class="sr-only">Our Taxi Services</h2>')
        self.assertContains(response, 'class="sr-only">Our Fleet</h2>')
        self.assertContains(response, 'aria-hidden="true"')

        # Redundant aria-labels should NOT be on submit buttons
        self.assertNotContains(response, 'aria-label="Send booking request"')
        self.assertNotContains(response, 'aria-label="Submit your review"')
