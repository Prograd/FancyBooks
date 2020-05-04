from graphene.test import Client
from snapshottest.django import TestCase

from graphqlAPI import schema


class UserEndpointTest(TestCase):

    def test_create_user(self):
        client = Client(schema.schema)
        self.assertMatchSnapshot(client.execute('''
            mutation {
                createUser(email: "test@test.test", username: "test", password: "test123" ) {
                user {
                  email
                  username
                }
              }
            }
        '''))
