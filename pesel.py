from faker import Faker

faker = Faker('pl_PL')  # ustawienie generatora w języku polskim

pesel = faker.pesel()

print(pesel)
