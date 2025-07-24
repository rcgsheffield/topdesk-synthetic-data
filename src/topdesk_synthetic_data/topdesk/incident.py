import random
import uuid
from datetime import timedelta

import faker

# Initialize Faker for realistic data generation
fake = faker.Faker()


class Incident:
    @classmethod
    def generate(cls, num_records=100):
        """
        Generate dummy data matching TOPdesk incident export structure
        Based on common TOPdesk fields from research
        """

        # TOPdesk status options
        statuses = [
            "firstLine",
            "secondLine",
            "partial",
            "resolved",
            "closed",
            "onHold",
        ]

        # Priority levels (typically 1-5, where 1 is highest)
        priorities = ["P1", "P2", "P3", "P4", "P5"]

        # Impact levels
        impacts = ["Person", "Department", "Site", "Infrastructure"]

        # Urgency levels
        urgencies = ["Low", "Normal", "High", "Urgent"]

        # Categories and subcategories
        categories = [
            "Hardware",
            "Software",
            "Network",
            "Access Management",
            "Email",
            "Printing",
            "Telephony",
            "Facilities",
        ]

        subcategories = {
            "Hardware": ["Desktop", "Laptop", "Monitor", "Printer", "Server"],
            "Software": [
                "Microsoft Office",
                "Operating System",
                "Browser",
                "Antivirus",
                "Application",
            ],
            "Network": ["Internet", "WiFi", "VPN", "File Share", "Speed"],
            "Access Management": [
                "Password Reset",
                "Account Creation",
                "Permissions",
                "VPN Access",
            ],
            "Email": ["Cannot Send", "Cannot Receive", "Outlook Issues", "Spam"],
            "Printing": ["Cannot Print", "Paper Jam", "Toner", "Driver Issues"],
            "Telephony": ["Cannot Call", "Voicemail", "Conference Call", "Mobile"],
            "Facilities": ["Heating", "Lighting", "Security", "Cleaning"],
        }

        # Entry types
        entry_types = ["Email", "Phone", "Self Service", "Walk-in", "Chat"]

        # Call types
        call_types = ["Incident", "Service Request", "Information Request"]

        # Operators (IT staff names)
        operators = [
            "John Smith",
            "Sarah Johnson",
            "Mike Brown",
            "Lisa Davis",
            "David Wilson",
            "Emma Taylor",
            "James Anderson",
            "Sophie White",
        ]

        # Generate the data
        data = []

        for i in range(num_records):
            # Generate call number (typical TOPdesk format: I YYMM NNN)
            call_number = f"I {random.randint(2401, 2412)} {str(i + 1).zfill(3)}"

            # Random dates within last 6 months
            call_date = fake.date_time_between(start_date="-6m", end_date="now")

            # Select category and corresponding subcategory
            category = random.choice(categories)
            subcategory = random.choice(subcategories[category])

            # Generate closed date (if status is closed/resolved)
            status = random.choice(statuses)
            closed_date = None
            target_date = call_date + timedelta(days=random.randint(1, 30))

            if status in ["closed", "resolved"]:
                closed_date = call_date + timedelta(
                    hours=random.randint(1, 72), minutes=random.randint(0, 59)
                )

            # Generate realistic brief description based on category
            brief_descriptions = {
                "Hardware": [
                    f"{subcategory} not working",
                    f"{subcategory} replacement needed",
                    f"{subcategory} slow performance",
                ],
                "Software": [
                    f"{subcategory} crashes",
                    f"{subcategory} installation needed",
                    f"{subcategory} license issue",
                ],
                "Network": [
                    f"{subcategory} connection issues",
                    f"No {subcategory} access",
                    f"{subcategory} slow speed",
                ],
                "Access Management": [
                    f"{subcategory} required",
                    f"Cannot access system",
                    f"{subcategory} not working",
                ],
                "Email": [
                    f"{subcategory} problem",
                    f"Email {subcategory.lower()}",
                    f"Outlook {subcategory.lower()}",
                ],
                "Printing": [
                    f"{subcategory} issue",
                    f"Printer {subcategory.lower()}",
                    f"Print queue stuck",
                ],
                "Telephony": [
                    f"{subcategory} problem",
                    f"Phone {subcategory.lower()}",
                    f"Call quality issues",
                ],
                "Facilities": [
                    f"{subcategory} not working",
                    f"{subcategory} request",
                    f"{subcategory} maintenance",
                ],
            }

            brief_description = random.choice(brief_descriptions[category])

            # Generate duration (in hours)
            duration = round(random.uniform(0.5, 48.0), 2) if closed_date else None

            yield {
                # Core incident fields
                "id": str(uuid.uuid4()),
                "number": call_number,
                "externalNumber": (
                    f"EXT-{random.randint(1000, 9999)}" if random.random() > 0.7 else ""
                ),
                "briefDescription": brief_description,
                "status": status,
                # Dates and times
                "callDate": call_date.strftime("%Y-%m-%d %H:%M:%S"),
                "creationDate": call_date.strftime("%Y-%m-%d %H:%M:%S"),
                "modificationDate": (
                    call_date + timedelta(hours=random.randint(0, 24))
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "targetDate": target_date.strftime("%Y-%m-%d %H:%M:%S"),
                "closedDate": (
                    closed_date.strftime("%Y-%m-%d %H:%M:%S") if closed_date else ""
                ),
                # Classification
                "category": category,
                "subcategory": subcategory,
                "callType": random.choice(call_types),
                "entryType": random.choice(entry_types),
                # Priority and impact
                "priority": random.choice(priorities),
                "impact": random.choice(impacts),
                "urgency": random.choice(urgencies),
                # People
                "callerName": fake.name(),
                "callerEmail": fake.email(),
                "callerPhone": fake.phone_number(),
                "callerDepartment": fake.company(),
                "callerBranch": random.choice(
                    ["Main Office", "Branch A", "Branch B", "Remote"]
                ),
                "operator": random.choice(operators) if random.random() > 0.3 else "",
                "operatorGroup": random.choice(
                    ["Level 1", "Level 2", "Level 3", "Specialists"]
                ),
                # Request and action fields
                "request": f"{call_date.strftime('%d-%m-%Y %H:%M')} [{fake.name()}]: {fake.text(max_nb_chars=200)}",
                "action": (
                    fake.text(max_nb_chars=150)
                    if status in ["resolved", "closed"]
                    else ""
                ),
                # Additional fields
                "duration": duration,
                "costs": (
                    round(random.uniform(0, 500), 2) if random.random() > 0.8 else 0
                ),
                "onHold": random.choice([True, False]) if status == "onHold" else False,
                "completed": status in ["resolved", "closed"],
                "closed": status == "closed",
                # Object/Asset information (if applicable)
                "objectName": (
                    fake.word().title() + "-" + str(random.randint(100, 999))
                    if random.random() > 0.5
                    else ""
                ),
                "objectType": (
                    random.choice(["Desktop", "Laptop", "Server", "Printer", "Phone"])
                    if random.random() > 0.5
                    else ""
                ),
                "location": fake.city() + " - " + fake.building_number(),
                # SLA fields
                "slaDeadline": (
                    call_date + timedelta(hours=random.randint(4, 72))
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "slaViolated": (
                    random.choice([True, False])
                    if status in ["resolved", "closed"]
                    else False
                ),
            }
