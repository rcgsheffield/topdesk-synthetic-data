#!/usr/bin/env python

import argparse
import logging

import pandas

from topdesk_synthetic_data.topdesk import Asset, Incident, Person

DESCRIPTION = """
TOPdesk synthetic data generator
"""

logger = logging.getLogger(__name__)


def get_args() -> argparse.Namespace:
    """
    Command-line arguments
    https://docs.python.org/3/howto/argparse.html
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("--log_level", default="INFO")
    return parser.parse_args()


def main():
    args = get_args()
    logging.basicConfig(
        format="%(name)s:%(asctime)s:%(levelname)s:%(message)s", level=args.log_level
    )

    logger.info("Generating TOPdesk dummy data...")

    # Generate incident data
    incidents = pandas.DataFrame.from_records(Incident.generate())
    incidents.to_csv("topdesk_incidents_dummy.csv", index=False)
    logger.info("Wrote topdesk_incidents_dummy.csv")
    incidents.to_excel("topdesk_incidents_dummy.xlsx", index=False)
    logger.info("Wrote topdesk_incidents_dummy.xlsx")

    # Generate person data
    people = pandas.DataFrame.from_records(Person.generate())
    people.to_csv("topdesk_persons_dummy.csv", index=False)
    logger.info("Wrote topdesk_persons_dummy.csv")
    people.to_excel("topdesk_persons_dummy.xlsx", index=False)
    logger.info("Wrote topdesk_persons_dummy.xlsx")

    # Generate asset data
    assets = pandas.DataFrame.from_records(Asset.generate())
    assets.to_csv("topdesk_assets_dummy.csv", index=False)
    logger.info("Wrote topdesk_assets_dummy.csv")
    assets.to_excel("topdesk_assets_dummy.xlsx", index=False)
    logger.info("Wrote topdesk_assets_dummy.xlsx")


if __name__ == "__main__":
    main()
