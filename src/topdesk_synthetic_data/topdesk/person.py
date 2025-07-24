import random
import uuid

import faker

fake = faker.Faker()


class Person:
    @classmethod
    def generate(cls, num_records=50):
        """
        Generate dummy data for TOPdesk person/employee export
        """

        departments = [
            "IT",
            "HR",
            "Finance",
            "Marketing",
            "Sales",
            "Operations",
            "Legal",
            "Facilities",
            "R&D",
            "Customer Service",
        ]

        branches = [
            "Head Office",
            "Branch North",
            "Branch South",
            "Branch East",
            "Branch West",
        ]

        for i in range(num_records):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = f"{first_name.lower()}.{last_name.lower()}@company.com"

            yield {
                "id": str(uuid.uuid4()),
                "dynamicName": f"{first_name} {last_name}",
                "firstName": first_name,
                "surName": last_name,
                "email": email,
                "loginName": f"{first_name.lower()}.{last_name.lower()}",
                "phoneNumber": fake.phone_number(),
                "mobileNumber": fake.phone_number(),
                "department": random.choice(departments),
                "branch": random.choice(branches),
                "location": fake.address().replace("\n", ", "),
                "jobTitle": fake.job(),
                "manager": fake.name(),
                "employeeNumber": f"EMP{str(i + 1).zfill(4)}",
                "startDate": fake.date_between(
                    start_date="-5y", end_date="today"
                ).strftime("%Y-%m-%d"),
                "endDate": (
                    fake.date_between(start_date="today", end_date="+2y").strftime(
                        "%Y-%m-%d"
                    )
                    if random.random() > 0.9
                    else ""
                ),
                "budgetHolder": fake.name(),
                "archived": (
                    random.choice([True, False]) if random.random() > 0.95 else False
                ),
            }
