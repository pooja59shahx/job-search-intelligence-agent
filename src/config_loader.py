from pathlib import Path

import yaml


ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT_DIR / "config"


def load_yaml(filename):
    """Load a YAML configuration file."""
    path = CONFIG_DIR / filename

    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_search_keywords():
    return load_yaml("search_keywords.yaml")


def load_companies():
    return load_yaml("companies.yaml")


def load_scoring_rules():
    return load_yaml("scoring_rules.yaml")


if __name__ == "__main__":
    print("Search Keywords:")
    print(load_search_keywords())

    print("\nCompanies:")
    print(load_companies())

    print("\nScoring Rules:")
    print(load_scoring_rules())
