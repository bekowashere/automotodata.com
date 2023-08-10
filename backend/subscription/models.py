from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User, ClientUser
from datetime import date, timedelta

class Plan(models.Model):
    name = models.CharField(_('Plan Name'), max_length=48)
    description = models.TextField(_('Description'), null=True, blank=True)
    slug = models.SlugField(_('Slug'), unique=True)
    daily_request = models.IntegerField(_('Daily Request Limit'), blank=True, null=True)
    price = models.DecimalField(
        _('Price'),
        max_digits=9,
        decimal_places=2
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')

class PlanFeature(models.Model):
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name="features",
        verbose_name=_('Plan')
    )
    feature_name = models.CharField(_('Feature Name'), max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.plan.name} - {self.feature_name}"
    
    class Meta:
        verbose_name = _('Plan Feature')
        verbose_name_plural = _('Plan Features')

class Subscription(models.Model):
    FREE = 'F'
    MONTHLY = 'M'
    YEARLY = 'Y'

    PERIOD_CHOICES = [
        (FREE, 'Free Trial'),
        (MONTHLY, 'Monthly Subscription'),
        (YEARLY, 'Yearly Subscription')
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_subscription",
        verbose_name=_('User')
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name="plan_subscriptions",
        verbose_name=_('Plan')
    )

    period_type = models.CharField(
        _('Period Type'),
        max_length=1,
        choices=PERIOD_CHOICES,
        default=FREE
    )
    period_duration = models.PositiveSmallIntegerField(
        _('Period Duration'),
        help_text=_('The default value is 30 because a month has 30 days. expiry_date = start_date + period_duration'),
        default=30
    )

    start_date = models.DateField(_('Start Date'), default=date.today())
    expiry_date = models.DateField(_('Expiry Date'), null=True, blank=True)

    paid_amount = models.DecimalField(
        _('Paid Amount'),
        max_digits=9,
        decimal_places=2
    )

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.user.email} - {self.plan.name}"
    
    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')