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
        Generate dummy data for research computing support incidents
        Focused on HPC, data management, training, and research IT needs
        """

        # Research computing specific statuses
        statuses = [
            "firstLine",
            "secondLine",
            "resolved",
            "closed",
            "onHold",
            "escalated"
        ]

        # Priority levels for research support
        priorities = ["P1", "P2", "P3", "P4", "P5"]

        # Impact levels relevant to research
        impacts = ["Individual Researcher", "Research Group", "Department", "Multi-Department", "University-wide"]

        # Urgency levels
        urgencies = ["Low", "Normal", "High", "Urgent", "Critical"]

        # Research computing categories
        categories = [
            "HPC Access & Authentication",
            "Data Management",
            "Software & Applications",
            "Training & Documentation",
            "Research Infrastructure",
            "Collaboration Tools",
            "Security & Compliance",
            "Hardware Resources"
        ]

        subcategories = {
            "HPC Access & Authentication": [
                "Login Issues", "SSH Key Problems", "Account Creation",
                "Password Reset", "Multi-factor Authentication", "VPN Access"
            ],
            "Data Management": [
                "Shared Storage Access", "Data Transfer", "Backup & Recovery",
                "File Permissions", "Quota Issues", "Data Migration"
            ],
            "Software & Applications": [
                "Module Loading", "Software Installation", "License Issues",
                "Conda/Python Environments", "R Packages", "MATLAB Toolboxes",
                "Containerization", "Version Conflicts"
            ],
            "Training & Documentation": [
                "HPC Training", "Python Programming", "R Programming",
                "Linux Command Line", "Job Scheduling", "Data Analysis",
                "Machine Learning", "Bioinformatics", "Documentation Request"
            ],
            "Research Infrastructure": [
                "Job Scheduling", "Queue Issues", "Resource Allocation",
                "GPU Access", "High Memory Jobs", "Parallel Computing",
                "Workflow Management", "Performance Optimization"
            ],
            "Collaboration Tools": [
                "JupyterHub", "RStudio Server", "Git/GitHub",
                "Shared Notebooks", "Version Control", "Code Sharing"
            ],
            "Security & Compliance": [
                "Data Security", "GDPR Compliance", "Ethical Approval",
                "Access Controls", "Audit Requirements", "Data Classification"
            ],
            "Hardware Resources": [
                "Compute Nodes", "Storage Systems", "Network Issues",
                "GPU Hardware", "Specialized Equipment", "Maintenance Windows"
            ]
        }

        # Entry types for research support
        entry_types = ["Email", "Self Service Portal", "Walk-in", "Video Call", "Slack", "Teams"]

        # Call types specific to research
        call_types = [
            "Technical Issue", "Service Request", "Training Request",
            "Consultation", "Data Request", "Access Request"
        ]

        # Research IT support staff
        operators = [
            "Dr. Sarah Chen", "Mark Thompson", "Dr. Lisa Rodriguez",
            "James Wright", "Dr. Emma Foster", "Alex Kumar",
            "Dr. Michael Singh", "Rachel Adams", "Tom Bradley"
        ]

        # Research departments and groups
        departments = [
            "Computer Science", "Physics", "Chemistry", "Biology",
            "Mathematics", "Engineering", "Psychology", "Economics",
            "Medicine", "Environmental Science", "Statistics", "Linguistics"
        ]

        # Academic positions
        academic_positions = [
            "Professor", "Associate Professor", "Assistant Professor",
            "Postdoc", "PhD Student", "Research Fellow",
            "Research Associate", "Master's Student", "Research Assistant"
        ]

        for i in range(num_records):
            # Generate call number (research IT format)
            call_number = f"RIT {random.randint(2401, 2412)} {str(i + 1).zfill(3)}"

            # Random dates within last 6 months
            call_date = fake.date_time_between(start_date="-6m", end_date="now")

            # Select category and corresponding subcategory
            category = random.choice(categories)
            subcategory = random.choice(subcategories[category])

            # Generate closed date (if status is closed/resolved)
            status = random.choice(statuses)
            closed_date = None
            target_date = call_date + timedelta(days=random.randint(1, 14))

            if status in ["closed", "resolved"]:
                closed_date = call_date + timedelta(
                    hours=random.randint(1, 120), minutes=random.randint(0, 59)
                )

            # Generate realistic brief descriptions for research computing
            brief_descriptions = {
                "HPC Access & Authentication": [
                    f"Cannot login to HPC cluster - {subcategory}",
                    f"SSH authentication failing - {subcategory}",
                    f"Need new HPC account - {subcategory}",
                    f"VPN connection issues for cluster access"
                ],
                "Data Management": [
                    f"Cannot access research data share - {subcategory}",
                    f"Need to mount /research/groupname directory",
                    f"Data transfer failing from local machine",
                    f"Backup of large dataset required - {subcategory}"
                ],
                "Software & Applications": [
                    f"Python environment not working - {subcategory}",
                    f"Cannot load required software module",
                    f"R package installation failing - {subcategory}",
                    f"MATLAB license error on cluster",
                    f"Docker container won't run - {subcategory}"
                ],
                "Training & Documentation": [
                    f"Request for {subcategory} workshop",
                    f"Need help with {subcategory} for research project",
                    f"Documentation missing for {subcategory}",
                    f"Training session needed for research group"
                ],
                "Research Infrastructure": [
                    f"Job not starting in queue - {subcategory}",
                    f"Need GPU resources for machine learning",
                    f"High memory job requirements - {subcategory}",
                    f"Parallel job optimization help needed"
                ],
                "Collaboration Tools": [
                    f"JupyterHub not accessible - {subcategory}",
                    f"Cannot share notebook with collaborators",
                    f"Git repository setup needed - {subcategory}",
                    f"RStudio Server connection issues"
                ],
                "Security & Compliance": [
                    f"Data security review required - {subcategory}",
                    f"GDPR compliance check for dataset",
                    f"Access control setup for sensitive data",
                    f"Ethics approval data handling guidance"
                ],
                "Hardware Resources": [
                    f"Compute node performance issues - {subcategory}",
                    f"Storage system slow response",
                    f"GPU hardware allocation request",
                    f"Network connectivity problems on cluster"
                ]
            }

            brief_description = random.choice(brief_descriptions[category])

            # Generate duration (research support often takes longer)
            duration = round(random.uniform(0.5, 72.0), 2) if closed_date else None

            # Generate research-specific caller information
            caller_department = random.choice(departments)
            caller_position = random.choice(academic_positions)
            caller_name = fake.name()

            # Create academic email
            name_parts = caller_name.lower().split()
            caller_email = f"{name_parts[0]}.{name_parts[-1]}@university.ac.uk"

            # Generate research-focused request text
            research_requests = [
                f"I'm working on a {fake.catch_phrase().lower()} project and need help with {subcategory.lower()}.",
                f"My research group is experiencing issues with {subcategory.lower()} on the HPC cluster.",
                f"We have a grant deadline approaching and need urgent help with {subcategory.lower()}.",
                f"I'm analyzing {fake.word()} data and encountering problems with {subcategory.lower()}.",
                f"Our {caller_department} research requires assistance with {subcategory.lower()}.",
                f"I'm a {caller_position.lower()} working on {fake.bs()} and need support with {subcategory.lower()}."
            ]

            request_text = f"{call_date.strftime('%d-%m-%Y %H:%M')} [{caller_name}]: {random.choice(research_requests)}"

            # Generate research-appropriate action text
            research_actions = [
                f"Provided step-by-step guidance for {subcategory.lower()} setup.",
                f"Scheduled training session for research group on {subcategory.lower()}.",
                f"Fixed configuration issue and tested {subcategory.lower()} functionality.",
                f"Created documentation and shared resources for {subcategory.lower()}.",
                f"Escalated to specialist team for advanced {subcategory.lower()} support.",
                f"Collaborated with researcher to optimize {subcategory.lower()} workflow.",
                f"Implemented solution and arranged follow-up meeting."
            ]

            action_text = random.choice(research_actions) if status in ["resolved", "closed"] else ""

            # Research-specific object names
            research_objects = [
                "HPC-Login-Node-01", "GPU-Cluster-A100", "Research-Storage-NFS",
                "JupyterHub-Server", "Conda-Environment", "SLURM-Queue",
                "Research-VPN", "Data-Share-Mount", "Docker-Registry"
            ]

            yield {
                # Core incident fields
                "id": str(uuid.uuid4()),
                "number": call_number,
                "externalNumber": (
                    f"GRANT-{random.randint(1000, 9999)}" if random.random() > 0.8 else ""
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
                "callType": random.choice(call_types),
                "entryType": random.choice(entry_types),
                # Priority and impact
                "priority": random.choice(priorities),
                "impact": random.choice(impacts),
                "urgency": random.choice(urgencies),
                # People (research-focused)
                "callerName": caller_name,
                "callerEmail": caller_email,
                "callerPhone": fake.phone_number(),
                "callerDepartment": caller_department,
                "callerPosition": caller_position,
                "callerBranch": random.choice(
                    ["Main Campus", "Science Park", "Medical School", "Engineering Building"]
                ),
                "researchGroup": f"{fake.last_name()} Lab",
                "grantCode": f"EP/{random.choice(['R', 'M', 'S'])}{random.randint(100000, 999999)}/1" if random.random() > 0.6 else "",
                "operator": random.choice(operators) if random.random() > 0.2 else "",
                "operatorGroup": random.choice(
                    ["Research Computing", "Data Management", "Training Team", "Infrastructure"]
                ),
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
                    random.choice(research_objects)
                    if random.random() > 0.4
                    else ""
                ),
                "objectType": (
                    random.choice(
                        ["HPC Cluster", "Storage System", "Software Environment", "Network Service", "Compute Node"])
                    if random.random() > 0.4
                    else ""
                ),
                "location": random.choice([
                    "Data Centre - Rack A12", "HPC Facility - Room 101",
                    "Research Building - Floor 3", "Virtual Infrastructure",
                    "Cloud Environment", "Network Core"
                ]),
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
                "researchDiscipline": random.choice([
                    "Computational Biology", "Machine Learning", "Data Science",
                    "High Energy Physics", "Climate Modeling", "Bioinformatics",
                    "Digital Humanities", "Computational Chemistry", "Social Science Analytics"
                ]),
                "softwareRequired": random.choice([
                    "Python/Anaconda", "R/RStudio", "MATLAB", "Mathematica",
                    "ANSYS", "COMSOL", "TensorFlow", "PyTorch", "Gaussian",
                    "GROMACS", "ImageJ", "Stata", "SPSS", "Custom Software"
                ]) if random.random() > 0.5 else "",
                "trainingRequired": random.choice([True, False]) if category == "Training & Documentation" else False,
                "followUpNeeded": random.choice([True, False]) if random.random() > 0.7 else False
            }
