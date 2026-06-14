from typing import Any
import os


def parse_coordinates(value: str) -> tuple[int, int]:
    try:
        x, y = value.split(",")
        return int(x), int(y)
    except ValueError as e:
        raise ValueError(f"Invalid coordinate format: {value}") from e


def parse_bool(value: str) -> bool:
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    raise ValueError(f"Invalid boolean value: {value}")


def parser_config(filename: str) -> dict[str, Any]:
    config: dict[str, Any] = {}

    mandatory_keys = {
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT",
    }

    optional_keys = {
        "SEED",
        "PATTERN_42",
    }

    all_keys = mandatory_keys | optional_keys

    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not exist")

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(f"Invalid line: {line}")

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if key not in all_keys:
                raise ValueError(f"Unknown configuration key: {key}")

            config[key] = value

    missing_keys = mandatory_keys - config.keys()
    if missing_keys:
        raise ValueError(f"Missing keys: {', '.join(sorted(missing_keys))}")

    # Type conversion
    try:
        config["WIDTH"] = int(config["WIDTH"])
        config["HEIGHT"] = int(config["HEIGHT"])

        if config["WIDTH"] <= 0:
            raise ValueError("WIDTH must be greater than 0")

        if config["HEIGHT"] <= 0:
            raise ValueError("HEIGHT must be greater than 0")

        config["ENTRY"] = parse_coordinates(config["ENTRY"])
        config["EXIT"] = parse_coordinates(config["EXIT"])

        config["PERFECT"] = parse_bool(config["PERFECT"])

        if "SEED" in config and config["SEED"]:
            config["SEED"] = int(config["SEED"])

        if "PATTERN_42" in config and config["PATTERN_42"]:
            config["PATTERN_42"] = parse_bool(config["PATTERN_42"])

    except ValueError as e:
        raise ValueError(f"Invalid configuration: {e}") from e

    # Coordinate validation
    entry_x, entry_y = config["ENTRY"]
    exit_x, exit_y = config["EXIT"]

    if not (
        0 <= entry_x < config["WIDTH"]
        and 0 <= entry_y < config["HEIGHT"]
    ):
        raise ValueError("ENTRY is outside maze bounds")

    if not (
        0 <= exit_x < config["WIDTH"]
        and 0 <= exit_y < config["HEIGHT"]
    ):
        raise ValueError("EXIT is outside maze bounds")

    if config["ENTRY"] == config["EXIT"]:
        raise ValueError("ENTRY and EXIT must be different")

    return config