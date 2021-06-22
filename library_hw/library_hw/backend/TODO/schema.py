import graphene
from graphene_django import DjangoObjectType
from .models import *


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_todo = graphene.List(TODOType)
    all_projects = graphene.List(ProjectType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    todo_by_id = graphene.Field(TODOType, id=graphene.Int(required=True))
    todo_by_authorname = graphene.List(TODOType, author=graphene.String(required=True))
    todo_by_project = graphene.List(TODOType, project=graphene.Int(required=True))

    @staticmethod
    def resolve_all_users(self, info):
        return CustomUser.objects.all()

    @staticmethod
    def resolve_all_todo(self, info):
        return TODO.objects.all()

    @staticmethod
    def resolve_all_projects(self, info):
        return Project.objects.all()

    @staticmethod
    def resolve_user_by_id(root, info, id):
        return CustomUser.objects.get(id=id)

    @staticmethod
    def resolve_project_by_id(root, info, id):
        return Project.objects.get(id=id)

    @staticmethod
    def resolve_todo_by_authorname(root, info, author=None):
        todo = TODO.objects.all()
        if author:
            todo = TODO.objects.filter(author__email=author)
        return todo

    @staticmethod
    def resolve_todo_by_project(root, info, project):
        todo = TODO.objects.all()
        if project:
            todo = TODO.objects.filter(project=project)
        return todo


schema = graphene.Schema(query=Query)
