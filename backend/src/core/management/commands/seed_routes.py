import json
from django.core.management.base import BaseCommand
from core.models import RoutePage

class Command(BaseCommand):
    help = 'Seeds initial SEO route pages for popular routes.'

    def handle(self, *args, **options):
        routes = [
            {
                'slug': 'gwalior-to-delhi-cab',
                'title': 'Gwalior to Delhi Cab Service — ₹4500 One-Way | Manjari Taxi',
                'meta_description': 'Book a reliable and comfortable Gwalior to Delhi cab with Manjari Taxi. Clean cars, professional drivers, and affordable fares starting at just ₹4500.',
                'h1_heading': 'Gwalior to Delhi Cab',
                'intro_text': 'Looking for a comfortable and hassle-free ride from Gwalior to Delhi? Manjari Taxi offers premium outstation cab services tailored to your needs. Whether you are traveling for business, a family trip, or catching an international flight from IGI Airport, we ensure a smooth journey.\n\nOur fleet includes well-maintained sedans and SUVs, driven by experienced professionals who prioritize your safety and comfort. With transparent pricing and no hidden charges, your Gwalior to Delhi trip has never been easier to plan.',
                'distance_km': 345,
                'duration_hours': 6.5,
                'starting_price': 4500,
                'is_published': True,
                'faq_json': [
                    {'question': 'How much does a Gwalior to Delhi cab cost?', 'answer': 'Our one-way fares for Gwalior to Delhi start at approximately ₹4500 for a sedan. SUV rates may vary.'},
                    {'question': 'How long does the journey take?', 'answer': 'The drive from Gwalior to Delhi usually takes around 6.5 hours depending on traffic and weather conditions via the Taj Express Highway/Yamuna Expressway.'},
                    {'question': 'Can I book a cab to Delhi IGI Airport?', 'answer': 'Yes, we provide direct airport transfers from Gwalior to Indira Gandhi International Airport (IGI) in Delhi.'}
                ]
            },
            {
                'slug': 'gwalior-to-agra-cab',
                'title': 'Gwalior to Agra Cab Service — Quick & Affordable | Manjari Taxi',
                'meta_description': 'Planning a trip to the Taj Mahal? Book a Gwalior to Agra cab with Manjari Taxi. Professional drivers and affordable rates for a comfortable 2.5-hour journey.',
                'h1_heading': 'Gwalior to Agra Cab',
                'intro_text': 'Need a quick and comfortable ride to Agra? Manjari Taxi provides reliable cab services from Gwalior to Agra, perfect for tourists visiting the Taj Mahal or business travelers. Enjoy a scenic and smooth drive on well-maintained roads in our premium cabs.\n\nWe offer flexible options including one-way drops and round-trip packages so you can explore Agra at your own pace.',
                'distance_km': 120,
                'duration_hours': 2.5,
                'starting_price': 2000,
                'is_published': True,
                'faq_json': [
                    {'question': 'Is it possible to book a round-trip from Gwalior to Agra?', 'answer': 'Absolutely! We offer customized round-trip packages that allow you to explore Agra and return comfortably.'},
                    {'question': 'Are toll taxes included in the fare?', 'answer': 'Typically, toll taxes and parking fees are extra and paid directly to the authorities, but we can provide an all-inclusive quote upon request.'}
                ]
            },
            {
                'slug': 'gwalior-to-jaipur-cab',
                'title': 'Gwalior to Jaipur Cab — Outstation Taxi | Manjari Taxi',
                'meta_description': 'Travel from Gwalior to Jaipur comfortably with Manjari Taxi. Offering well-maintained sedans and SUVs for your Rajasthan trip.',
                'h1_heading': 'Gwalior to Jaipur Cab',
                'intro_text': 'Experience the vibrant culture of the Pink City with Manjari Taxi. Our Gwalior to Jaipur cab service is designed for maximum comfort on long journeys. Whether you are planning a weekend getaway or a long vacation in Rajasthan, our experienced drivers know the best routes to ensure a safe and timely arrival.\n\nChoose from our wide range of vehicles, from economical sedans for small families to spacious SUVs for group travel.',
                'distance_km': 335,
                'duration_hours': 6.5,
                'starting_price': 5500,
                'is_published': True,
                'faq_json': [
                    {'question': 'What types of cars are available for the Jaipur trip?', 'answer': 'We offer a variety of vehicles including sedans (Dzire, Etios) and SUVs (Innova, Ertiga) to suit your comfort and luggage requirements.'},
                    {'question': 'Do you provide night driving services?', 'answer': 'Yes, our experienced drivers are available for night journeys, ensuring your safety throughout the trip.'}
                ]
            },
            {
                'slug': 'gwalior-airport-taxi',
                'title': 'Gwalior Airport Taxi Service — Fast & Reliable | Manjari Taxi',
                'meta_description': 'Looking for a reliable airport transfer? Book our Gwalior Airport taxi service for timely pickups and drop-offs. Available 24/7.',
                'h1_heading': 'Gwalior Airport Taxi',
                'intro_text': 'Never miss a flight with Manjari Taxi. We provide prompt and reliable airport transfer services to and from Gwalior Airport (Rajmata Vijaya Raje Scindia Air Terminal). Our drivers track your flight status to ensure timely pickups, even if your flight is delayed.\n\nEnjoy a stress-free start or end to your journey with our clean, comfortable cabs and professional service. Available 24/7 for all early morning or late-night flights.',
                'distance_km': 15,
                'duration_hours': 0.5,
                'starting_price': 600,
                'is_published': True,
                'faq_json': [
                    {'question': 'Can I pre-book a cab for an early morning flight?', 'answer': 'Yes, we highly recommend pre-booking for early morning flights. Our service is available 24/7.'},
                    {'question': 'Will the driver wait if my flight is delayed?', 'answer': 'Yes, we track flight schedules and our drivers will adjust their arrival time accordingly.'}
                ]
            }
        ]

        for data in routes:
            page, created = RoutePage.objects.update_or_create(
                slug=data['slug'],
                defaults=data
            )
            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f'{action} route page: {page.slug}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded route pages.'))
