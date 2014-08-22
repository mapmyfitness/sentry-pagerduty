import sentry_pagerduty
import pygerduty
from sentry_pagerduty.forms import PagerDutyConfigForm
from sentry.plugins.bases.notify import NotifyPlugin


class PagerDutyPlugin(NotifyPlugin):
    """
    Sentry plugin to send errors stats to Pagerduty.
    """
    author = 'Depop developers'
    author_url = 'https://github.com/depop/sentry-pagerduty'
    version = sentry_pagerduty.VERSION
    description = 'Send error occurence to Pagerduty.'
    slug = 'pagerduty'
    title = 'Pagerduty'
    conf_key = slug
    conf_title = title
    resource_links = [
        ('Source', 'https://github.com/depop/sentry-pagerduty'),
        ('Bug Tracker', 'https://github.com/depop/sentry-pagerduty/issues'),
        ('README', 'https://github.com/depop/sentry-pagerduty/blob/master/README.rst'),
    ]
    project_conf_form = PagerDutyConfigForm

    def is_configured(self, project, **kwargs):
        params = self.get_option
        return (params('api_key', project) and
                params('service_key', project) and
                params('domain_name', project))

    def on_alert(self, alert, **kwargs):
        if not self.is_configured(alert.project):
            return

        if not self.get_option('notify_on_alert'):
            return

        self.trigger_incident(
            alert.project,
            alert.message,
            incident_key='sentry-alert-%i' % alert.id
        )

    def notify_users(self, group, event, fail_silently=False):
        if not self.is_configured(group.project):
            return

        if not self.get_option('notify_on_event'):
            return

        self.trigger_incident(
            group.project,
            event.message,
            incident_key='sentry-%i' % group.id
        )

    def trigger_incident(self, project, message, incident_key):
        api_key = self.get_option('api_key', project)
        domain_name = self.get_option('domain_name', project)
        service_key = self.get_option('service_key', project)

        client = pygerduty.PagerDuty(domain_name, api_key)
        client.trigger_incident(service_key, message, incident_key=incident_key)

