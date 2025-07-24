import random
import uuid
from datetime import timedelta
from typing import Any, Dict, Generator

import faker

# Initialize Faker for realistic data generation
fake = faker.Faker()


class Incident:
    """Generator for research computing support incident dummy data"""

    # Research computing specific statuses
    STATUSES = [
        "In Progress",
        "Logged",
        "Resolved",
        "Waiting for user",
        "Monitored call",
        "We think we have resolved",
    ]

    # Priority levels for research support
    PRIORITIES = ["P1", "P2", "P3", "P4", "RFC"]

    # Impact levels relevant to research
    IMPACTS = [
        "Person",
        "Team",
        "Lecture",
        "Department",
        "University",
    ]

    # Urgency levels
    URGENCIES = ["Low", "Medium", "High", "RFC", "Critical"]

    # Research computing categories
    CATEGORIES = [
        "HPC Access & Authentication",
        "Data Management",
        "Software & Applications",
        "Training & Documentation",
        "Research Infrastructure",
        "Collaboration Tools",
        "Security & Compliance",
        "Hardware Resources",
    ]

    SUBCATEGORIES = {
        "HPC Access & Authentication": [
            "Login Issues",
            "SSH Key Problems",
            "Account Creation",
            "Password Reset",
            "Multi-factor Authentication",
            "VPN Access",
        ],
        "Data Management": [
            "Shared Storage Access",
            "Data Transfer",
            "Backup & Recovery",
            "File Permissions",
            "Quota Issues",
            "Data Migration",
        ],
        "Software & Applications": [
            "Module Loading",
            "Software Installation",
            "License Issues",
            "Conda/Python Environments",
            "R Packages",
            "MATLAB Toolboxes",
            "Containerization",
            "Version Conflicts",
        ],
        "Training & Documentation": [
            "HPC Training",
            "Python Programming",
            "R Programming",
            "Linux Command Line",
            "Job Scheduling",
            "Data Analysis",
            "Machine Learning",
            "Bioinformatics",
            "Documentation Request",
        ],
        "Research Infrastructure": [
            "Job Scheduling",
            "Queue Issues",
            "Resource Allocation",
            "GPU Access",
            "High Memory Jobs",
            "Parallel Computing",
            "Workflow Management",
            "Performance Optimization",
        ],
        "Collaboration Tools": [
            "JupyterHub",
            "RStudio Server",
            "Git/GitHub",
            "Shared Notebooks",
            "Version Control",
            "Code Sharing",
        ],
        "Security & Compliance": [
            "Data Security",
            "GDPR Compliance",
            "Ethical Approval",
            "Access Controls",
            "Audit Requirements",
            "Data Classification",
        ],
        "Hardware Resources": [
            "Compute Nodes",
            "Storage Systems",
            "Network Issues",
            "GPU Hardware",
            "Specialized Equipment",
            "Maintenance Windows",
        ],
    }

    # Entry types for research support
    ENTRY_TYPES = [
        "Email",
        "Self Service Portal",
        "Walk-in",
        "Video Call",
        "Slack",
        "Teams",
    ]

    # Call types specific to research
    CALL_TYPES = [
        "Technical Issue",
        "Service Request",
        "Training Request",
        "Consultation",
        "Data Request",
        "Access Request",
    ]

    # Research IT support staff
    OPERATORS = [
        "Dr. Sarah Chen",
        "Mark Thompson",
        "Dr. Lisa Rodriguez",
        "James Wright",
        "Dr. Emma Foster",
        "Alex Kumar",
        "Dr. Michael Singh",
        "Rachel Adams",
        "Tom Bradley",
    ]

    # Research departments and groups
    DEPARTMENTS = [
        "Computer Science",
        "Physics",
        "Chemistry",
        "Biology",
        "Mathematics",
        "Engineering",
        "Psychology",
        "Economics",
        "Medicine",
        "Environmental Science",
        "Statistics",
        "Linguistics",
    ]

    # Academic positions
    ACADEMIC_POSITIONS = [
        "Professor",
        "Associate Professor",
        "Assistant Professor",
        "Postdoc",
        "PhD Student",
        "Research Fellow",
        "Research Associate",
        "Master's Student",
        "Research Assistant",
    ]

    # Campus locations
    CAMPUS_BRANCHES = [
        "Main Campus",
        "Science Park",
        "Medical School",
        "Engineering Building",
    ]

    # Research infrastructure objects
    RESEARCH_OBJECTS = [
        "HPC-Login-Node-01",
        "GPU-Cluster-A100",
        "Research-Storage-NFS",
        "JupyterHub-Server",
        "Conda-Environment",
        "SLURM-Queue",
        "Research-VPN",
        "Data-Share-Mount",
        "Docker-Registry",
    ]

    # Object types
    OBJECT_TYPES = [
        "HPC Cluster",
        "Storage System",
        "Software Environment",
        "Network Service",
        "Compute Node",
    ]

    # Locations
    LOCATIONS = [
        "Data Centre - Rack A12",
        "HPC Facility - Room 101",
        "Research Building - Floor 3",
        "Virtual Infrastructure",
        "Cloud Environment",
        "Network Core",
    ]

    # Research disciplines
    RESEARCH_DISCIPLINES = [
        "Computational Biology",
        "Machine Learning",
        "Data Science",
        "High Energy Physics",
        "Climate Modeling",
        "Bioinformatics",
        "Digital Humanities",
        "Computational Chemistry",
        "Social Science Analytics",
    ]

    # Software commonly used in research
    RESEARCH_SOFTWARE = [
        "Python/Anaconda",
        "R/RStudio",
        "MATLAB",
        "Mathematica",
        "ANSYS",
        "COMSOL",
        "TensorFlow",
        "PyTorch",
        "Gaussian",
        "GROMACS",
        "ImageJ",
        "Stata",
        "SPSS",
        "Custom Software",
    ]

    # Operator groups
    OPERATOR_GROUPS = [
        "Research Computing",
        "Data Management",
        "Training Team",
        "Infrastructure",
    ]

    @classmethod
    def reference_number(cls) -> str:
        return f"SHEF {random.randint(1000, 9999)} {random.randint(1000, 9999)}"

    @classmethod
    def generate(cls, num_records: int = 100) -> Generator[Dict[str, Any], None, None]:
        """
        Generate dummy data for research computing support incidents

        Args:
            num_records: Number of incident records to generate

        Yields:
            Dict containing incident data matching TOPdesk structure
        """

        for i in range(num_records):

            # Random dates within last 6 months
            call_date = fake.date_time_between(start_date="-6m", end_date="now")

            # Select category and corresponding subcategory
            category = random.choice(cls.CATEGORIES)
            subcategory = random.choice(cls.SUBCATEGORIES[category])

            # Generate closed date (if status is closed/resolved)
            status = random.choice(cls.STATUSES)
            closed_date = None
            target_date = call_date + timedelta(days=random.randint(1, 14))

            if status in ["closed", "resolved"]:
                closed_date = call_date + timedelta(
                    hours=random.randint(1, 120), minutes=random.randint(0, 59)
                )

            # Generate realistic brief description
            brief_description = cls._generate_brief_description(category, subcategory)

            # Generate duration (research support often takes longer)
            duration = round(random.uniform(0.5, 72.0), 2) if closed_date else None

            # Generate research-specific caller information
            caller_department = random.choice(cls.DEPARTMENTS)
            caller_position = random.choice(cls.ACADEMIC_POSITIONS)
            caller_name = fake.name()

            # Create academic email
            name_parts = caller_name.lower().split()
            caller_email = f"{name_parts[0]}.{name_parts[-1]}@university.ac.uk"

            # Generate research-focused request and action text
            request_text = cls._generate_request_text(
                call_date, caller_name, subcategory, caller_department, caller_position
            )
            action_text = cls._generate_action_text(subcategory, status)

            yield {
                # Core incident fields
                "id": str(uuid.uuid4()),
                "number": cls.reference_number(),
                "externalNumber": (
                    f"GRANT-{random.randint(1000, 9999)}"
                    if random.random() > 0.8
                    else ""
                ),
                "briefDescription": brief_description,
                "status": status,
                # Dates and times
                "callDate": call_date.strftime("%Y-%m-%d %H:%M:%S"),
                "creationDate": call_date.strftime("%Y-%m-%d %H:%M:%S"),
                "modificationDate": (
                    call_date + timedelta(hours=random.randint(0, 48))
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "targetDate": target_date.strftime("%Y-%m-%d %H:%M:%S"),
                "closedDate": (
                    closed_date.strftime("%Y-%m-%d %H:%M:%S") if closed_date else ""
                ),
                # Classification
                "category": category,
                "subcategory": subcategory,
                "callType": random.choice(cls.CALL_TYPES),
                "entryType": random.choice(cls.ENTRY_TYPES),
                # Priority and impact
                "priority": random.choice(cls.PRIORITIES),
                "impact": random.choice(cls.IMPACTS),
                "urgency": random.choice(cls.URGENCIES),
                # People (research-focused)
                "callerName": caller_name,
                "callerEmail": caller_email,
                "callerPhone": fake.phone_number(),
                "callerDepartment": caller_department,
                "callerPosition": caller_position,
                "callerBranch": random.choice(cls.CAMPUS_BRANCHES),
                "researchGroup": f"{fake.last_name()} Lab",
                "grantCode": cls._generate_grant_code(),
                "operator": (
                    random.choice(cls.OPERATORS) if random.random() > 0.2 else ""
                ),
                "operatorGroup": random.choice(cls.OPERATOR_GROUPS),
                # Request and action fields
                "request": request_text,
                "action": action_text,
                # Additional fields
                "duration": duration,
                "costs": (
                    round(random.uniform(0, 200), 2) if random.random() > 0.9 else 0
                ),
                "onHold": random.choice([True, False]) if status == "onHold" else False,
                "completed": status in ["resolved", "closed"],
                "closed": status == "closed",
                # Research infrastructure objects
                "objectName": (
                    random.choice(cls.RESEARCH_OBJECTS) if random.random() > 0.4 else ""
                ),
                "objectType": (
                    random.choice(cls.OBJECT_TYPES) if random.random() > 0.4 else ""
                ),
                "location": random.choice(cls.LOCATIONS),
                # SLA fields (research support typically has longer SLAs)
                "slaDeadline": (
                    call_date + timedelta(hours=random.randint(24, 168))  # 1-7 days
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "slaViolated": (
                    random.choice([True, False])
                    if status in ["resolved", "closed"]
                    else False
                ),
                # Research-specific fields
                "researchDiscipline": random.choice(cls.RESEARCH_DISCIPLINES),
                "softwareRequired": (
                    random.choice(cls.RESEARCH_SOFTWARE)
                    if random.random() > 0.5
                    else ""
                ),
                "trainingRequired": (
                    random.choice([True, False])
                    if category == "Training & Documentation"
                    else False
                ),
                "followUpNeeded": (
                    random.choice([True, False]) if random.random() > 0.7 else False
                ),
            }

    @classmethod
    def _generate_brief_description(cls, category: str, subcategory: str) -> str:
        """Generate realistic brief descriptions for research computing issues"""
        brief_descriptions = {
            "HPC Access & Authentication": [
                f"Cannot login to HPC cluster - {subcategory}",
                f"SSH authentication failing - {subcategory}",
                f"Need new HPC account - {subcategory}",
                "VPN connection issues for cluster access",
            ],
            "Data Management": [
                f"Cannot access research data share - {subcategory}",
                "Need to mount /research/groupname directory",
                "Data transfer failing from local machine",
                f"Backup of large dataset required - {subcategory}",
            ],
            "Software & Applications": [
                f"Python environment not working - {subcategory}",
                "Cannot load required software module",
                f"R package installation failing - {subcategory}",
                "MATLAB license error on cluster",
                f"Docker container won't run - {subcategory}",
            ],
            "Training & Documentation": [
                f"Request for {subcategory} workshop",
                f"Need help with {subcategory} for research project",
                f"Documentation missing for {subcategory}",
                "Training session needed for research group",
            ],
            "Research Infrastructure": [
                f"Job not starting in queue - {subcategory}",
                "Need GPU resources for machine learning",
                f"High memory job requirements - {subcategory}",
                "Parallel job optimization help needed",
            ],
            "Collaboration Tools": [
                f"JupyterHub not accessible - {subcategory}",
                "Cannot share notebook with collaborators",
                f"Git repository setup needed - {subcategory}",
                "RStudio Server connection issues",
            ],
            "Security & Compliance": [
                f"Data security review required - {subcategory}",
                "GDPR compliance check for dataset",
                "Access control setup for sensitive data",
                "Ethics approval data handling guidance",
            ],
            "Hardware Resources": [
                f"Compute node performance issues - {subcategory}",
                "Storage system slow response",
                "GPU hardware allocation request",
                "Network connectivity problems on cluster",
            ],
        }
        return random.choice(brief_descriptions[category])

    @classmethod
    def _generate_request_text(
        cls,
        call_date,
        caller_name: str,
        subcategory: str,
        caller_department: str,
        caller_position: str,
    ) -> str:
        """Generate research-focused request text"""
        research_requests = [
            f"I'm working on a {fake.catch_phrase().lower()} project and need help with {subcategory.lower()}.",
            f"My research group is experiencing issues with {subcategory.lower()} on the HPC cluster.",
            f"We have a grant deadline approaching and need urgent help with {subcategory.lower()}.",
            f"I'm analyzing {fake.word()} data and encountering problems with {subcategory.lower()}.",
            f"Our {caller_department} research requires assistance with {subcategory.lower()}.",
            f"I'm a {caller_position.lower()} working on {fake.bs()} and need support with {subcategory.lower()}.",
        ]
        return f"{call_date.strftime('%d-%m-%Y %H:%M')} [{caller_name}]: {random.choice(research_requests)}"

    @classmethod
    def _generate_action_text(cls, subcategory: str, status: str) -> str:
        """Generate research-appropriate action text"""
        if status not in ["resolved", "closed"]:
            return ""

        research_actions = [
            f"Provided step-by-step guidance for {subcategory.lower()} setup.",
            f"Scheduled training session for research group on {subcategory.lower()}.",
            f"Fixed configuration issue and tested {subcategory.lower()} functionality.",
            f"Created documentation and shared resources for {subcategory.lower()}.",
            f"Escalated to specialist team for advanced {subcategory.lower()} support.",
            f"Collaborated with researcher to optimize {subcategory.lower()} workflow.",
            "Implemented solution and arranged follow-up meeting.",
        ]
        return random.choice(research_actions)

    @classmethod
    def _generate_grant_code(cls) -> str:
        """Generate UK research council grant code format"""
        if random.random() > 0.6:
            council = random.choice(["EP", "MR", "ST", "BB", "NE", "ES", "AH"])
            return f"{council}/{random.choice(['R', 'M', 'S'])}{random.randint(100000, 999999)}/1"
        return ""
