import factory

from django.contrib.auth.models import User

from django.utils import timezone


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_%d" % n)

    # last_login = factory.Faker('date')
    last_login = factory.LazyFunction(timezone.now)
