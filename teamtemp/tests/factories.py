__author__ = 'traviswarren'

import factory

from datetime import datetime

from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.hashers import make_password

from teamtemp.responses.models import TeamTemperature, TemperatureResponse, User


class DjangoUserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = DjangoUser
    FACTORY_DJANGO_GET_OR_CREATE = ('username',)

    username = factory.Sequence(lambda n: 'user%d' % n)
    password = make_password('password')
    is_active = True
    is_staff = False


class UserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = User
    FACTORY_DJANGO_GET_OR_CREATE = ('id',)

    id = factory.Sequence(lambda n: n)


class TeamTemperatureFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = TeamTemperature
    FACTORY_DJANGO_GET_OR_CREATE = ('creator', 'creation_date')

    creator = factory.SubFactory(DjangoUserFactory)
    creation_date = datetime.now()


class TeamResponseFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = TemperatureResponse
    FACTORY_DJANGO_GET_OR_CREATE = ('request', 'responder')

    request = factory.SubFactory(TeamTemperatureFactory)
    responder = factory.SubFactory(UserFactory)
    score = 5
    word = 'word'
