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

    # Common research data types and file formats
    RESEARCH_DATA_TYPES = [
        "genomic sequences",
        "climate model outputs",
        "survey responses",
        "microscopy images",
        "sensor readings",
        "text corpora",
        "financial data",
        "experimental measurements",
        "simulation results",
        "log files",
    ]

    # File formats commonly used in research
    FILE_FORMATS = [
        ".csv",
        ".xlsx",
        ".hdf5",
        ".netcdf",
        ".fasta",
        ".bam",
        ".tiff",
        ".json",
        ".xml",
        ".mat",
        ".rds",
        ".pkl",
        ".zarr",
    ]

    # Common research computing tools and environments
    COMPUTING_TOOLS = [
        "Jupyter notebooks",
        "conda environments",
        "Docker containers",
        "SLURM job scripts",
        "makefiles",
        "shell scripts",
        "R packages",
    ]

    # Error messages commonly seen in research computing
    ERROR_MESSAGES = [
        "Permission denied",
        "Module not found",
        "Out of memory",
        "Connection timeout",
        "File not found",
        "License checkout failed",
        "Segmentation fault",
        "Authentication failed",
        "Disk quota exceeded",
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

            # Generate detailed incident body (the actual user submission)
            incident_body = cls._generate_incident_body(
                category, subcategory, caller_name, caller_position, caller_department
            )

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
                "incidentBody": incident_body,  # Full user submission text
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

    @classmethod
    def _generate_incident_body(
        cls,
        category: str,
        subcategory: str,
        caller_name: str,
        caller_position: str,
        caller_department: str,
    ) -> str:
        """Generate detailed incident body text (the actual user submission)"""

        # Templates for different categories of incidents
        body_templates = {
            "HPC Access & Authentication": [
                f"""Hello,

I'm having trouble accessing the HPC cluster. When I try to log in using:
ssh {fake.user_name()}@cluster.university.ac.uk

I get the error: "{random.choice(cls.ERROR_MESSAGES)}"

I've tried:
- Checking my network connection
- Using different terminals (PuTTY, Terminal, WSL)
- Regenerating my SSH keys

My project deadline is approaching and I really need access to run my {fake.word()} analysis scripts.

Could someone please help?

Best regards,
{caller_name}
{caller_position}, {caller_department}""",
                f"""Hi Research Computing Team,

I need a new account on the HPC system for my research project on {fake.bs()}.

My supervisor is Prof. {fake.last_name()} and I'm working on grant {cls._generate_grant_code() or 'pending approval'}.

I will need:
- Access to the {random.choice(['gpu', 'highmem', 'general'])} queue
- Storage quota of approximately {random.randint(100, 2000)}GB
- Software: {random.choice(cls.RESEARCH_SOFTWARE)}

When can I expect the account to be ready?

Thanks,
{caller_name}""",
                f"""Support team,

My SSH keys seem to have stopped working suddenly. Yesterday everything was fine, but today I'm getting authentication
failures.

Error message: "{random.choice(cls.ERROR_MESSAGES)}"

I'm in the middle of running a large batch of jobs for a conference deadline next week. Is there a quick fix for this?

I'm available for a call if that helps troubleshoot faster.

{caller_name}
{caller_department}""",
            ],
            "Data Management": [
                f"""Dear Research IT,

I'm trying to access our research group's shared data directory at /research/{fake.word()}_lab/ but getting permission
errors.

I need to access approximately {random.randint(10, 500)}GB of {random.choice(cls.RESEARCH_DATA_TYPES)} stored in
{random.choice(cls.FILE_FORMATS)} format.

The error I'm seeing is: "{random.choice(cls.ERROR_MESSAGES)}"

My supervisor Prof. {fake.last_name()} said I should have access. Can you please check my permissions?

This data is critical for my {caller_position.lower()} research on {fake.bs()}.

Many thanks,
{caller_name}""",
                f"""Hello,

I need help transferring a large dataset ({random.randint(50, 1000)}GB) from my local workstation to the cluster
storage.

I've tried using rsync but the transfer keeps failing after a few hours:
rsync -avz --progress /local/data/ cluster:/research/data/

Error: "{random.choice(cls.ERROR_MESSAGES)}"

Is there a better method for large file transfers? The dataset contains {random.choice(cls.RESEARCH_DATA_TYPES)} in
multiple {random.choice(cls.FILE_FORMATS)} files.

Any advice would be appreciated!

{caller_name}
{caller_position}, {caller_department}""",
                f"""Hi team,

I accidentally deleted some important research data from /research/{fake.word()}_project/

The files were:
- {fake.word()}_analysis{random.choice(cls.FILE_FORMATS)}
- {fake.word()}_results{random.choice(cls.FILE_FORMATS)}
- Several folders of {random.choice(cls.RESEARCH_DATA_TYPES)}

This happened yesterday around {fake.time()}. Do you have backups I can restore from?

This is for a grant application due next week - please help!

Urgently,
{caller_name}""",
            ],
            "Software & Applications": [
                f"""Research Computing Support,

I'm having issues with my Python environment on the cluster. When I try to run my analysis script, I get:

```
ModuleNotFoundError: No module named '{fake.word()}'
```

I've tried:
- module load python/3.{random.randint(8, 11)}
- pip install {fake.word()}
- Creating a new conda environment

But nothing seems to work. My script worked fine last month.

I'm analyzing {random.choice(cls.RESEARCH_DATA_TYPES)} for my {caller_position.lower()} thesis and really need this
working.

Can someone help troubleshoot?

Best,
{caller_name}
{caller_department}""",
                f"""Hello,

I need help installing {random.choice(cls.RESEARCH_SOFTWARE)} on the cluster for my research group.

We need this for our {fake.bs()} project. The software requires:
- {random.choice(['GPU support', 'MPI libraries', 'Large memory', 'Special libraries'])}
- License: {random.choice(['Academic', 'Open source', 'Commercial - we have license'])}

I tried installing it myself but got: "{random.choice(cls.ERROR_MESSAGES)}"

Could you please install this system-wide or help me with a local installation?

Timeline: We need this working by {fake.date_between(start_date='today', end_date='+1m').strftime('%Y-%m-%d')} for our
paper submission.

Thanks,
{caller_name}""",
                f"""Support Team,

I'm getting MATLAB license errors when trying to run jobs on the cluster:

"License checkout failed for {fake.word()}_Toolbox"

This is blocking my research on {fake.bs()}. The jobs were working fine until this week.

My SLURM script:
```
#!/bin/bash
#SBATCH --job-name={fake.word()}_job
#SBATCH --time=12:00:00
#SBATCH --mem=32G

module load matlab
matlab -batch "run_analysis('{fake.word()}')"
```

Can you check the license server status?

{caller_name}
{caller_position}""",
            ],
            "Training & Documentation": [
                f"""Dear Training Team,

I'm a new {caller_position.lower()} in {caller_department} and need help getting started with the HPC cluster.

I have basic Linux knowledge but I'm new to:
- Job scheduling with SLURM
- Loading software modules
- Managing large datasets
- {random.choice(['Python parallel processing', 'R on clusters', 'GPU programming'])}

Is there a workshop or training session I can attend? I learn better in group settings than reading documentation alone.

My research involves {fake.bs()} and I'll be working with {random.choice(cls.RESEARCH_DATA_TYPES)}.

Please let me know what training options are available.

Thanks,
{caller_name}""",
                f"""Hi Research Computing,

Our research group (Prof. {fake.last_name()}'s lab) would like to request a training session on {subcategory.lower()}.

We have {random.randint(3, 12)} people at various levels:
- {random.randint(1, 3)} {random.choice(cls.ACADEMIC_POSITIONS).lower()}s
- {random.randint(2, 6)} PhD students
- {random.randint(1, 4)} postdocs

We're particularly interested in:
- Best practices for {random.choice(cls.COMPUTING_TOOLS)}
- Optimizing code performance
- Managing research workflows

Could we schedule something for next week? We can provide coffee and biscuits!

Best regards,
{caller_name}
{caller_department}""",
                f"""Hello,

I'm struggling to find documentation for {subcategory.lower()} on the cluster.

Specifically, I need help with:
- Setting up {random.choice(cls.COMPUTING_TOOLS)}
- Configuring {random.choice(cls.RESEARCH_SOFTWARE)}
- Best practices for {random.choice(['data analysis', 'parallel computing', 'job optimization'])}

The existing documentation seems outdated (references old software versions).

Could someone either:
1. Point me to current documentation, or
2. Create updated guides for these topics?

I'm happy to help write documentation based on what I learn!

{caller_name}
{caller_position}, {caller_department}""",
            ],
            "Research Infrastructure": [
                f"""HPC Support,

My job has been stuck in the queue for {random.randint(24, 72)} hours:

```
JOBID PARTITION     NAME     USER ST       TIME  NODES
{random.randint(1000000, 9999999)}   {random.choice(['gpu', 'highmem', 'general'])}     {fake.word()}_job
{fake.user_name()}  PD       0:00      1
```

Job script summary:
- Memory: {random.randint(64, 512)}GB
- Time: {random.randint(12, 72)}:00:00  
- GPUs: {random.randint(1, 4) if 'gpu' in str(random.choice(['gpu', 'cpu'])) else 0}

Is this normal queue time? My conference deadline is in two weeks.

Can you advise on optimizing the resource request or suggest alternative queues?

Thanks,
{caller_name}""",
                f"""Research Computing Team,

I need help optimizing my parallel job. It's running much slower than expected on the cluster.

Current performance:
- Local desktop (8 cores): {random.randint(2, 6)} hours
- Cluster (32 cores): {random.randint(8, 20)} hours (expected ~30 minutes)

The job processes {random.choice(cls.RESEARCH_DATA_TYPES)} using {random.choice(cls.RESEARCH_SOFTWARE)}.

I suspect it's not scaling properly. Could someone help profile the job and suggest optimizations?

I can provide the code and sample data for testing.

{caller_name}
{caller_department}""",
                f"""Hello,

I'm requesting access to GPU resources for my machine learning research.

Project details:
- Deep learning training on {random.choice(['image', 'text', 'sensor'])} data
- Framework: {random.choice(['TensorFlow', 'PyTorch', 'JAX'])}
- Expected runtime: {random.randint(24, 168)} hours per experiment
- GPU memory needed: {random.choice(['12GB+', '24GB+', '32GB+'])}

My supervisor is Prof. {fake.last_name()} and we have funding from grant {cls._generate_grant_code() or 'pending'}.

What's the process for GPU queue access?

{caller_name}
{caller_position}""",
            ],
            "Collaboration Tools": [
                f"""Support Team,

I can't access JupyterHub at https://jupyter.cluster.university.ac.uk

Error message: "{random.choice(cls.ERROR_MESSAGES)}"

I was working on an important notebook yesterday for my {fake.bs()} analysis. The notebook contains several hours of work processing {random.choice(cls.RESEARCH_DATA_TYPES)}.

Is the service down? When will it be restored?

I need to complete this analysis by {fake.date_between(start_date='+1d', end_date='+1w').strftime('%Y-%m-%d')} for a project meeting.

{caller_name}
{caller_department}""",
                f"""Hi Research IT,

I need help setting up a shared Git repository for our research group.

Requirements:
- {random.randint(3, 10)} collaborators from {caller_department}
- Code in {random.choice(['Python', 'R', 'MATLAB', 'C++'])}
- Some data files (~{random.randint(1, 50)}GB)
- Need access from both cluster and local machines

Should we use:
- GitHub with university account?
- GitLab on local servers?
- Something else?

Also need guidance on:
- Best practices for research code repositories
- Handling large data files
- Managing different software environments

Thanks for any advice!

{caller_name}""",
                f"""Research Computing,

I'm trying to share a Jupyter notebook with my collaborators but having issues.

The notebook analyses {random.choice(cls.RESEARCH_DATA_TYPES)} and needs access to:
- Cluster storage at /research/{fake.word()}_data/
- {random.choice(cls.RESEARCH_SOFTWARE)} modules
- About {random.randint(8, 64)}GB RAM

How can multiple people work on this simultaneously? We're in different time zones so need asynchronous collaboration.

Is there a shared notebook server option?

{caller_name}
{caller_position}, {caller_department}""",
            ],
            "Security & Compliance": [
                f"""Data Protection Team,

I need guidance on handling sensitive research data on the cluster.

Data type: {random.choice(['Human subjects survey data', 'Medical imaging data', 'Personal interview transcripts',
                           'Financial records', 'Genomic data'])}
Ethics approval: {fake.bothify('ETH####')}
Data subjects: ~{random.randint(100, 5000)} individuals

Questions:
- What storage location should I use?
- Do I need special access controls?
- Are there logging requirements?
- How should data be anonymized?

The research is for my {caller_position.lower()} project on {fake.bs()}.

Please advise on compliance requirements.

{caller_name}
{caller_department}""",
                f"""Security Team,

I received a data security warning about my recent cluster usage. The email mentioned "unusual data access patterns"
but wasn't specific.

What I was doing:
- Downloading {random.randint(10, 100)}GB of {random.choice(cls.RESEARCH_DATA_TYPES)}
- Running analysis scripts from {fake.date_between(start_date='-1w', end_date='now').strftime('%Y-%m-%d')}
- Accessing data from multiple cluster nodes

This is all legitimate research activity for my {fake.bs()} project.

Can someone clarify what triggered the warning and how to avoid it in future?

{caller_name}""",
                f"""Compliance Team,

I need to ensure my research data handling meets GDPR requirements.

Project: {fake.bs()}
Data: Survey responses from EU residents ({random.randint(50, 500)} subjects)
Storage: Currently on cluster at /research/{fake.word()}_survey/

Questions:
- Is the current storage location compliant?
- Do I need additional consent for computational analysis?
- How long can I retain the data?
- What are the deletion requirements?

Ethics committee has approved the research but didn't provide specific technical guidance.

{caller_name}
{caller_position}, {caller_department}""",
            ],
            "Hardware Resources": [
                f"""Infrastructure Team,

I'm experiencing very slow performance on compute node {fake.word()}-{random.randint(10, 99)}.

Symptoms:
- Jobs taking {random.randint(3, 10)}x longer than usual
- High I/O wait times
- Memory allocation errors

My job normally processes {random.choice(cls.RESEARCH_DATA_TYPES)} in {random.randint(2, 8)} hours but it's been
running for {random.randint(24, 72)} hours.

Can you check if there's a hardware issue with this node?

Job ID: {random.randint(1000000, 9999999)}

{caller_name}""",
                f"""Hardware Support,

The storage system seems very slow today. File operations that usually take minutes are taking hours.

Affected operations:
- Reading {random.choice(cls.FILE_FORMATS)} files from /research/
- Writing analysis results 
- Basic file listing (ls commands)

This is impacting multiple people in our {caller_department} research group.

Is there a known storage issue? Any estimated resolution time?

We have a project deadline approaching and need reliable data access.

{caller_name}
{caller_department}""",
                f"""Maintenance Team,

When is the next scheduled maintenance window for the cluster?

I have a large computational job that will take approximately {random.randint(48, 168)} hours to complete.
I want to time it to avoid any planned downtime.

The job analyzes {random.choice(cls.RESEARCH_DATA_TYPES)} for my {fake.bs()} research.

Also, will the maintenance affect:
- Login nodes?
- Storage systems?  
- Software modules?

Thanks for the heads up!

{caller_name}""",
            ],
        }

        # Select appropriate templates for the category
        templates = body_templates.get(
            category,
            [
                f"""Hello,

I'm having an issue with {subcategory.lower()} and need assistance.

I'm a {caller_position.lower()} in {caller_department} working on {fake.bs()}.

Please help resolve this as soon as possible.

{caller_name}"""
            ],
        )

        return random.choice(templates)
