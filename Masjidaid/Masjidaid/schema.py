import graphene
import masjidaidsapp.schema
from masjidaidsapp.schema import Query as masjids_query


class Query(masjids_query, graphene.ObjectType):
    pass

class Mutation(masjidaidsapp.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
# 