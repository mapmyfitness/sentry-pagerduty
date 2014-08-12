# coding: utf-8
"""
sentry_pagerduty.forms
"""
from django import forms

COUNT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('5', 5),
    ('10', 10),
    ('25', 25),
    ('50', 50),
    ('100', 100),
    ('250', 250),
    ('500', 500),
    ('1000', 1000),
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

    instance_counts = forms.TypedMultipleChoiceField(
        choices=COUNT_CHOICES,
        coerce=int,
        help_text="Trigger incidents at these group counts",
    )
