import graphene

from graphene_django.types import DjangoObjectType
from .models import User, Masjid, MasjidsImages


class UserType(DjangoObjectType):
    class Meta:
        model = User

class MasjidType(DjangoObjectType):
    class Meta:
        model = Masjid

class MasjidsImagesType(DjangoObjectType):
    class Meta:
        model = MasjidsImages

class Query(object):

    user = graphene.Field(
        UserType,
        id=graphene.ID(),
        first_name=graphene.String(),
        last_name=graphene.String(),
        email=graphene.Int(),
        mobile=graphene.String()
    )
    users = graphene.List(UserType)
    
    masjid = graphene.Field(
        MasjidType,
        id=graphene.ID(),
        name=graphene.String(),
        address=graphene.String(),
        lga=graphene.String(),
        lat_long=graphene.String(),
        state=graphene.String(),
        user_id=graphene.ID(),
        contact_name=graphene.String(),
        contact_number=graphene.String()
    )

    masjids = graphene.List(MasjidType)
    
    masjids_image = graphene.Field(
        MasjidsImagesType,
        id=graphene.ID(),
        images=graphene.String(),
        masjid_id=graphene.ID()
        )


    masjids_images = graphene.List(MasjidsImagesType)

    def resolve_user(self, info, **kwargs):
        id=kwargs.get('id')

        if id is not None:
            return User.objects.get(pk=id)

       
        return None

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_masjid(self, info, **kwargs):
        id=kwargs.get('id')
        name=kwargs.get('name')

        if id is not None:
            return Masjid.objects.get(pk=id) 
        if name is not None:
            return Masjid.objects.get(name=name)
        return None

    def resolve_masjids(self, info, **kwargs):
        return Masjid.objects.select_related('user_id').all()

    def resolve_masjids_image(self, info, **kwargs):
        id=kwargs.get('id')

        if id is not None:
            return MasjidsImages.objects.get(pk=id)
        return None

    def resolve_masjids_images(self, info, **kwargs):
        return MasjidsImages.objects.all()

# class User(graphene.ObjectType):
#     first_name=graphene.String(),
#     last_name=graphene.String(),
#     email=graphene.String(),
#     mobile=graphene.String(),
#     password=graphene.String()

# class AddUser(graphene.Mutation):
#         class Arguments:
#             user=graphene.Field(lambda: User)

#         def mutate(self, info, user_data=None):
#             user = User(
#                 first_name=user_data.first_name,
#                 last_name=user_data.last_name,
#                 email=user_data.email,
#                 mobile=user_data.mobile,
#                 password=user_data.password
#             )
#             return AddUser(user=user)