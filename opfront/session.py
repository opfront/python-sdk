from opfront.client import OpfrontClient
from opfront.order import OrderResource
from opfront.product import ProductResource
from opfront.resource import OpfrontResource
from opfront.user import UserResource


class OpfrontSession(object):

    """
    OpfrontSession defines the set of resources available from the Opfront API.
    Can be used as a standard object as and as a context manager.

    Args:
        email (str): Email with which to login
        password (str): Password associated with the email
    """

    def __init__(self, email, password, api_url='https://api.opfront.ca'):
        client = OpfrontClient(email, password, api_url=api_url)

        # Resource definition
        self.spectacle = OpfrontResource('/spectacles', client)
        self.store = OpfrontResource('/stores', client)
        self.product = ProductResource('/products', client)
        self.order = OrderResource('/orders', client)
        self.user = UserResource('/users', client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
