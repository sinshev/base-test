import basecrm
from .base_user import User


class LeadsAPICalls(object):
    """This class implements API calls for BaseCRM leads"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Singleton pattern"""
        if not cls._instance:
            cls._instance = super(LeadsAPICalls, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        user = User()
        self.client = basecrm.Client(access_token=user.get_access_token())

    def get_lead_id_by_full_name(self, first_name, last_name):
        leads_list = self.client.leads.list()
        for lead in leads_list:
            if lead["first_name"] == first_name and lead["last_name"] == last_name:
                return lead["id"]

    def delete_lead_by_id(self, id):
        self.client.leads.destroy(id=id)
