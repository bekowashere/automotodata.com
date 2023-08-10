from django.contrib import admin
from subscription.models import Plan, PlanFeature, Subscription
from django.utils.translation import gettext_lazy as _

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Plan Information'), {'fields': ('name', 'slug', 'daily_request', 'price', 'total_subscriptions_count', 'total_features_count')}),
        (_('Description'), {'fields': ('description',)})
    )
    list_display = ('slug', 'name', 'daily_request', 'price')
    search_fields = ('name', 'slug')
    ordering = ('price',)
    readonly_fields = ('total_subscriptions_count', 'total_features_count')

@admin.register(PlanFeature)
class PlanFeatureAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Plan Feature Information'), {'fields': ('plan',)}),
        (_('Feature Information'), {'fields': ('feature_name', 'description')}),
    )
    list_display = ('feature_name',)
    list_filter = ('plan',)
    search_fields = ('plan__name__icontains', 'plan__slug__icontains', 'feature_name')
    ordering = ('plan__name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Subscription Information'), {'fields': ('user', 'plan', 'is_active')}),
        (_('Period'), {'fields': ('period_type', 'period_duration')}),
        (_('Subscription Date'), {'fields': ('start_date', 'expiry_date')}),
        (_('Price'), {'fields': ('paid_amount',)}),
    )
    list_display = ('user', 'plan', 'period_type', 'start_date', 'expiry_date', 'is_active')
    list_filter = ('period_type', 'is_active')
    search_fields = ('user__email', 'plan__name')
    ordering = ('start_date',)