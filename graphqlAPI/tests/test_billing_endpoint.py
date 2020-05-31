from graphene.test import Client
from snapshottest.django import TestCase

from graphqlAPI import schema
from graphqlAPI.tests.data import initialize


class UserEndpointTest(TestCase):

    def test_create_billing(self):
        initialize()
        client = Client(schema.schema)
        self.assertMatchSnapshot(client.execute('''
            mutation {
              createBilling(books: [{id: 1, amount: 2}, {id: 2, amount: 2}, {id: 3, amount: 3}]) {
                billing {
                  id
                  status
                  order {
                    id
                    books {
                      id
                    }
                  }
                }
              }
            }
        '''))
