from faker import Faker

fake = Faker()


class Payloads:
    successful_registration = {
        'email': 'eve.holt@reqres.in',
        'password': fake.password(),
    }

    unsuccessful_registration = {
        'email': 'eve.holt@reqres.in',
    }