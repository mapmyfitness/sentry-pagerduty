# coding: utf-8
"""
sentry_pagerduty.forms
"""
from django import forms


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
    notify_on_alert = forms.BooleanField()
    notify_on_event = forms.BooleanField()
