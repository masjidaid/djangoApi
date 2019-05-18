import graphene

from masjidaidsapp.schema import Query as masjids_query
# AddUser as add_user


class Query(masjids_query, graphene.ObjectType):
    pass

# class Mutation(add_user, graphene.ObjectType):
    # pass

schema = graphene.Schema(query=Query)
# , mutation=Mutation