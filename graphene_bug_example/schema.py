from graphene_django import DjangoObjectType
import graphene

from graphene_bug_example.models import Example as ExampleModel


class Example(DjangoObjectType):
    required_field = graphene.String(required=True)

    class Meta:
        model = ExampleModel


class Query(graphene.ObjectType):
    examples = graphene.List(Example)

    def resolve_users(self, info):
        return UserModel.objects.all()

schema = graphene.Schema(query=Query)
