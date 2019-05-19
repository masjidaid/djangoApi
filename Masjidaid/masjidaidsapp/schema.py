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
        email=graphene.String(),
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


class AddUser(graphene.Mutation):
  
    class Arguments:
        first_name=graphene.String()
        last_name=graphene.String()
        email=graphene.String()
        mobile=graphene.String()
        password=graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, first_name, last_name, email, mobile, password):
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            password=password
        )
        user.save()
        return AddUser(
            user=user
            )

class AddMasjid(graphene.Mutation):
    class Arguments:
        name=graphene.String()
        address=graphene.String()
        lga=graphene.String()
        lat_long=graphene.String()
        state=graphene.String()
        user_id=graphene.String()
        contact_name=graphene.String()
        contact_number=graphene.String()
    
    masjid = graphene.Field(MasjidType)

    def mutate(self, info, name, address, lga, lat_long, state, user_id, contact_name, contact_number):
        masjid = Masjid(
            name=name,
            address=address,
            lga=lga,
            lat_long=lat_long,
            state=state,
            user_id=user_id,
            contact_name=contact_name,
            contact_number=contact_number
        )
        masjid.save()
        return AddMasjid(
            masjid=masjid
        )

class AddMasjidsImages(graphene.Mutation):
    class Arguments:
        images=graphene.String()
        masjid_id=graphene.String()

    masjid_images = graphene.Field(MasjidsImagesType)
    def mutate(self, info, images, masjid_id):
        masjid_images= MasjidsImages(
            images=images,
            masjid_id=masjid_id
        )
        masjid_images.save
        return AddMasjidsImages(masjid_images=masjid_images)

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    add_masjid = AddMasjid.Field()