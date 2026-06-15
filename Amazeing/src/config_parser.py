from typing import Any
import os


def parse_condinates(value: str) -> tuple[int, int]:
    try:
        x, y = value.split(",")
        return int(x.strip()), int(y.strip())
    except ValueError as e:
        raise ValueError(f"Invalid cordinate format: {value}") from e
    
def parse_bool(value: str) -> bool:
    cleaned = value.strip().lower()
    if cleaned == "true":
        return True
    if cleaned == "false":
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

    if not  os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not found: does not exit")
    
    
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line or  line.startswith("#"):
                continue
            if "=" not in line:
                raise ValueError(f"Missing '=' in {line} ")
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            if key not in all_keys:
                continue
            config[key] = value

        missing_keys = mandatory_keys - config.keys()
        if missing_keys:
            raise ValueError(f"MIssing keys: {', '.join(sorted(missing_keys))}")
        
        try:
            config["WIDTH"] = int(config["WIDTH"])
            config["HEIGHT"] = int(config["HEIGHT"])
            config["ENTRY"] = parse_condinates(config["ENTRY"])
            config["EXIT"] = parse_condinates(config["EXIT"])
            config["PERFECT"] = parse_bool(config["PERFECT"])

            if "SEED" in config:
                config["SEED"] = int(config["SEED"])
            else:
                config["SEED"] = 42

            if "PATTERN_42" in config:
                config["PATTERN_42"] = int(config["PATTERN_42"])

            else:
                config["PATTERN_42"] = 42

        except (ValueError, IndexError) as e:
            raise ValueError(f"Invalid configuaration: {e}") from e
        
    return config