from ScoutSuite.providers.azure.facade.base import AzureFacade
from ScoutSuite.providers.azure.resources.base import AzureResources


class Alerts(AzureResources):

    def __init__(self, facade: AzureFacade, subscription_id: str):
        super(Alerts, self).__init__(facade)
        self.subscription_id = subscription_id

    async def fetch_all(self):
        a = await self.facade.securitycenter.get_alerts(self.subscription_id)
        for raw_alert in a:
            id, alert = self._parse_alert(raw_alert)
            self[id] = alert

    def _parse_alert(self, alert):
        alert_dict = {}
        alert_dict['id'] = alert.id
        alert_dict['name'] = alert.name
        return alert_dict['id'], alert_dict
