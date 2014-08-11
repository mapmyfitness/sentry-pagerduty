# coding: utf-8
"""
sentry_pagerduty.forms
"""
from django import forms

COUNT_CHOICES = (
    '1',
    '2',
    '5',
    '10',
    '25',
    '50',
    '100',
    '250',
    '500',
    '1000'
)

class PagerDutyConfigForm(forms.Form):
    api_key = forms.CharField(
        max_length=255,
        help_text='Pagerduty API KEY'
    )

    service_key = forms.CharField(
        max_length=32,
        help_text="Pagerduty's Sentry service key"
    )

    domain_name = forms.CharField(
        max_length=255,
        help_text="Domain Name of your pagerduty instance (e.g. 'sterling_cooper')"
    )

    instance_counts = forms.MultipleChoiceField(
        choices=COUNT_CHOICES,
        default=COUNT_CHOICES,
        help_text="Trigger incidents at these group counts",
    )
