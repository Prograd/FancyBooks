from graphene.test import Client
from snapshottest.django import TestCase

from graphqlAPI import schema
from graphqlAPI.tests.data import initialize


class BookEndpointTest(TestCase):

    def test_get_all_books(self):
        initialize()
        client = Client(schema.schema)
        self.assertMatchSnapshot(client.execute('''
            {
              books {
                id
                title
                subtitle
                publisher
                publishedDate
                description
                pageCount
                thumbnailUrl
                language
                authors
                price
                categories {
                  id
                }
              }
            }
        '''))
