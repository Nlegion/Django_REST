import graphene
from graphene_django import DjangoObjectType
from .models import *


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_email = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_all_users(self, info):
        return CustomUser.objects.all()

    def resolve_user_by_id(self, info):
        return CustomUser.objects.get(id=id)


class UsersUpdateMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        id = graphene.ID()

    users = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, email, id):
        user = CustomUser.objects.get(id=id)
        user.email = email
        user.save()
        return UsersUpdateMutation(user)


class UsersCreateMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        is_superuser = graphene.Boolean(required=True)
        is_staff = graphene.Boolean(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, email, is_superuser, is_staff):
        user = CustomUser.objects.get(is_superuser=is_superuser, is_staff=is_staff, email=email)
        user.save()
        return UsersCreateMutation(user)


class Mutation(graphene.ObjectType):
    update_user = UsersUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=UsersUpdateMutation)
