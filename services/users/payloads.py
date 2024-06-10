from faker import Faker

fake = Faker()


class Payloads:
    user = {
        'name': fake.name(),
        'job': fake.job(),
    }