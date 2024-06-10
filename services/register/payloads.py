from faker import Faker

fake = Faker()


class Payloads:
    successful_registration = {
        'email': f'{fake.user_name()}@reqres.in',
        'password': fake.password(),
    }

    unsuccessful_registration = {
        'email': fake.email(),
    }