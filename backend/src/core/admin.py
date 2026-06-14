from django.contrib import admin
from .models import Service, Vehicle, Review, RoutePage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'css_class')
    search_fields = ('title', 'description')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'seats')
    list_filter = ('category',)
    search_fields = ('name', 'category')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'location', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'rating', 'created_at')
    search_fields = ('customer_name', 'location', 'review')
    list_editable = ('approved',)


@admin.register(RoutePage)
class RoutePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'starting_price', 'updated_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'slug', 'h1_heading')
    prepopulated_fields = {'slug': ('h1_heading',)}
    list_editable = ('is_published',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('SEO', {
            'fields': ('title', 'meta_description', 'slug'),
        }),
        ('Page Content', {
            'fields': ('h1_heading', 'intro_text', 'body_text'),
        }),
        ('Route Stats', {
            'fields': ('distance_km', 'duration_hours', 'starting_price'),
            'classes': ('collapse',),
        }),
        ('FAQ (Rich Snippets)', {
            'fields': ('faq_json',),
            'classes': ('collapse',),
        }),
        ('Publishing', {
            'fields': ('is_published', 'created_at', 'updated_at'),
        }),
    )
