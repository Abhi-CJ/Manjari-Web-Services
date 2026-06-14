from django.urls import path
from .views import home, submit_review, robots_txt, route_page

urlpatterns = [
    path('', home, name='home'),
    path('submit_review/', submit_review, name='submit_review'),
    path('robots.txt', robots_txt, name='robots_txt'),
    # SEO route pages — must be last (slug catch-all)
    path('<slug:slug>/', route_page, name='route_page'),
]

