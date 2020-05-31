from graphene import InputObjectType, Int


class BookInput(InputObjectType):
    id = Int(required=True)
    amount = Int(required=False)
