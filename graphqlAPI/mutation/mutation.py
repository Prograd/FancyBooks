import graphene
import graphql_jwt

from graphqlAPI.mutation.billing_create import BillingCreate
from graphqlAPI.mutation.user_create import CreateUser


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_billing = BillingCreate.Field()
    create_user = CreateUser.Field()
