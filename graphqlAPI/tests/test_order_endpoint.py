from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from graphene.test import Client
from snapshottest.django import TestCase

from graphqlAPI import schema
from graphqlAPI.tests.data import initialize


class OrderEndpointTest(TestCase):
    QUERY = '''
            {
              orders {
                id
                billing {
                  id
                }
                orderPrice
              }
            }
        '''

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_all_order_when_admin(self):
        initialize()
        client = Client(schema.schema)
        user = get_user_model()(
            username='test',
            email='test',
            is_superuser=True
        )
        user.save()
        self.factory.user = user
        self.assertMatchSnapshot(client.execute(self.QUERY, context_value=self.factory))

    def test_get_all_order_when_anonymous(self):
        initialize()
        client = Client(schema.schema)
        self.factory.user = AnonymousUser()
        self.assertMatchSnapshot(client.execute(self.QUERY, context_value=self.factory))
