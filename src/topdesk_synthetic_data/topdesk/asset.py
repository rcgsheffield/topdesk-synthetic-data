import random
import uuid

import faker

fake = faker.Faker()


class Asset:

    @classmethod
    def generate(cls, num_records: int = 100):
        """
        Generate dummy data for TOPdesk asset/configuration management export
        """

        asset_types = [
            "Desktop",
            "Laptop",
            "Server",
            "Printer",
            "Monitor",
            "Phone",
            "Tablet",
            "Switch",
            "Router",
        ]
        brands = [
            "Dell",
            "HP",
            "Lenovo",
            "Apple",
            "Microsoft",
            "Cisco",
            "Canon",
            "Samsung",
        ]
        statuses = ["In Use", "Available", "Broken", "In Repair", "Retired", "Ordered"]

        for i in range(num_records):
            asset_type = random.choice(asset_types)
            brand = random.choice(brands)

            yield {
                "id": str(uuid.uuid4()),
                "name": f"{brand} {asset_type} {str(i + 1).zfill(3)}",
                "type": asset_type,
                "brand": brand,
                "model": f"{brand}-{random.randint(1000, 9999)}",
                "serialNumber": fake.lexify(text="????-####-????").upper(),
                "assetTag": f"AST{str(i + 1).zfill(5)}",
                "status": random.choice(statuses),
                "location": fake.city() + " - Floor " + str(random.randint(1, 5)),
                "assignedTo": fake.name() if random.random() > 0.3 else "",
                "assignedToDepartment": random.choice(
                    ["IT", "HR", "Finance", "Marketing", "Sales"]
                ),
                "purchaseDate": fake.date_between(
                    start_date="-3y", end_date="today"
                ).strftime("%Y-%m-%d"),
                "purchasePrice": round(random.uniform(200, 3000), 2),
                "supplier": fake.company(),
                "warrantyDate": fake.date_between(
                    start_date="today", end_date="+3y"
                ).strftime("%Y-%m-%d"),
                "lastModified": fake.date_time_between(
                    start_date="-30d", end_date="now"
                ).strftime("%Y-%m-%d %H:%M:%S"),
            }
