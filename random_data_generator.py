from faker import Faker
import sys


def generate_users(count=10, locale="en_US"):
    fake = Faker(locale)
    users = []
    for _ in range(count):
        users.append({
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address().replace("\n", ", ")
        })
    return users


def generate_companies(count=10, locale="en_US"):
    fake = Faker(locale)
    companies = []
    for _ in range(count):
        companies.append({
            "company_name": fake.company(),
            "phone": fake.phone_number(),
            "address": fake.address().replace("\n", ", ")
        })
    return companies


if __name__ == "__main__":
    count = 10
    locale = "en_US"
    mode = "user"  # or 'company'

    # Example CLI:
    # python3 random_data_generator.py 5 de_AT company
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid number.")
            sys.exit(1)

    if len(sys.argv) > 2:
        locale = sys.argv[2]

    if len(sys.argv) > 3 and sys.argv[3].lower() == "company":
        mode = "company"

    print(f"🌍 Generating {count} fake {'companies' if mode == 'company' else 'users'} for locale: {locale}\n")

    if mode == "company":
        data = generate_companies(count, locale)
    else:
        data = generate_users(count, locale)

    for entry in data:
        print(entry)
