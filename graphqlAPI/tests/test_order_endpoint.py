from graphene.test import Client
from snapshottest.django import TestCase

from graphqlAPI import schema


class OrderEndpointTest(TestCase):

    def test_get_all_order(self):
        client = Client(schema.schema)
        self.assertMatchSnapshot(client.execute('''
            {
              orders {
                id
                billing {
                  id
                }
                orderPrice
              }
            }
        '''))
