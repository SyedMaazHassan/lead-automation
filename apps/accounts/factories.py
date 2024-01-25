import factory
from faker import Faker
from .models import Lead, Profile
from django.contrib.auth.models import User

fake = Faker()

class LeadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lead

    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    email = factory.LazyFunction(fake.email)
    phone = factory.LazyFunction(fake.phone_number)
    status = factory.LazyFunction(lambda: fake.random_element(elements=('New', 'Cold Email sent', 'Nurturing email sent', 'Closed', 'Responded')))
    background = factory.LazyFunction(fake.text)
    profile = factory.Iterator(Profile.objects.all())


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    username = factory.LazyFunction(fake.user_name)
    email = factory.LazyFunction(fake.email)
    password = factory.LazyFunction(fake.password)

