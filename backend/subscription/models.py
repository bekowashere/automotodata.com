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