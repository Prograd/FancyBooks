from graphqlAPI.mutation.mutation import Mutation
from graphqlAPI.query.query import Query

import graphene

schema = graphene.Schema(query=Query, mutation=Mutation)
