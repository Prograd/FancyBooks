from graphene.test import Client
from snapshottest.django import TestCase

from graphqlAPI import schema
from graphqlAPI.data import initialize


class CategoryEndpointTest(TestCase):

    def test_get_all_categories(self):
        initialize()
        client = Client(schema.schema)
        self.assertMatchSnapshot(client.execute('''
            {
              categories {
                id
                name
                bookSet{
                  id
                }
              }
            }
        '''))
