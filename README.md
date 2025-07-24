# TOPdesk synthetic data generator

A tool to generate dummy data to simulate [TOPdesk](https://docs.python.org/3/library/venv.html) ticket data exports. TOPdesk is a ticketing system for support services to manage user support queries.

The algorithms used to produce these synthetic data is random and not sourced from any real support requests. This tool uses the [Faker](https://faker.readthedocs.io/) library, with is a framework in the Python programming language used to generate dummy data.

# Installation

1. Install [Python](https://python.org)
2. Create a [virtual environment](https://docs.python.org/3/library/venv.html)

```bash
python -m venv .venv
```

3. Install this package

```bash
pip install git+https://github.com/rcgsheffield/topdesk-synthetic-data.git
```

# Usage

Once installed, run `topdesk-synthetic-data` in the command line.

```bash
topdesk-synthetic-data --help
```
```
usage: topdesk-synthetic-data [-h] [--log_level LOG_LEVEL] [--num_records NUM_RECORDS]

TOPdesk synthetic data generator

options:
  -h, --help            show this help message and exit
  --log_level LOG_LEVEL
  --num_records, -n NUM_RECORDS

```

## Example

```bash
topdesk-synthetic-data -n 100
```

# Contributing

Please read the [contribution guide](./CONTRIBUTING.md).
