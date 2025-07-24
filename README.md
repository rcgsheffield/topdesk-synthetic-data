# TOPdesk synthetic data generator

A tool to generate dummy data to simulate TOPdesk ticket data exports.

# Installation

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
