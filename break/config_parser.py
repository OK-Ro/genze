from typing import Any
import os


# ----------------------------
# Converters (safe + reusable)
# ----------------------------

def to_int(name: str, value: str) -> int:
    try:
        return int(value)
    except ValueError as e:
        raise ValueError(f"{name} must be an integer, got '{value}'") from e


def to_bool(name: str, value: str) -> bool:
    v = value.strip().lower()
    if v == "true":
        return True
    if v == "false":
        return False
    raise ValueError(f"{name} must be true/false, got '{value}'")


def to_coord(name: str, value: str) -> tuple[int, int]:
    try:
        x, y = value.split(",")
        return int(x.strip()), int(y.strip())
    except Exception as e:
        raise ValueError(f"{name} must be 'x,y', got '{value}'") from e


def get_default_int(config: dict[str, str], key: str, default: int) -> int:
    return int(config[key]) if key in config else default


# ----------------------------
# Main parser
# ----------------------------

def parser_config(filename: str) -> dict[str, Any]:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Config file '{filename}' does not exist")

    config: dict[str, str] = {}

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

    allowed_keys = mandatory_keys | optional_keys

    # ----------------------------
    # Step 1: read file
    # ----------------------------
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(f"Invalid line format: '{line}' (expected key=value)")

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if key not in allowed_keys:
                continue

            config[key] = value

    # ----------------------------
    # Step 2: check missing keys
    # ----------------------------
    missing = mandatory_keys - config.keys()
    if missing:
        raise ValueError(f"Missing required keys: {missing}")

    # ----------------------------
    # Step 3: convert types
    # ----------------------------
    try:
        width = to_int("WIDTH", config["WIDTH"])
        height = to_int("HEIGHT", config["HEIGHT"])

        entry = to_coord("ENTRY", config["ENTRY"])
        exit_point = to_coord("EXIT", config["EXIT"])

        perfect = to_bool("PERFECT", config["PERFECT"])

        seed = get_default_int(config, "SEED", 42)
        pattern_42 = get_default_int(config, "PATTERN_42", 42)

    except Exception as e:
        raise RuntimeError("Config type conversion failed") from e

    # ----------------------------
    # Step 4: validation rules
    # ----------------------------
    if width <= 0 or height <= 0:
        raise ValueError("WIDTH and HEIGHT must be > 0")

    if entry == exit_point:
        raise ValueError("ENTRY and EXIT cannot be the same")

    # ----------------------------
    # Step 5: return final typed config
    # ----------------------------
    return {
        "WIDTH": width,
        "HEIGHT": height,
        "ENTRY": entry,
        "EXIT": exit_point,
        "PERFECT": perfect,
        "SEED": seed,
        "PATTERN_42": pattern_42,
        "OUTPUT_FILE": config["OUTPUT_FILE"],
    }