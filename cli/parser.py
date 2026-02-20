CIPHER_ALIASES = {
    "caesar": "caesar",
    "ceaser": "caesar",
    "c": "caesar",
    "playfair": "playfair",
    "pf": "playfair",
    "rail_fence": "rail_fence",
    "railfence": "rail_fence",
    "rf": "rail_fence",
    "row_column": "row_column",
    "rowcolumn": "row_column",
    "rc": "row_column",
}

ATTACK_ALIASES = {
    "caesar": "caesar",
    "c": "caesar",
    "ceaser": "caesar",
    "rail_fence": "rail_fence",
    "railfence": "rail_fence",
    "rf": "rail_fence",
}

MODE_ALIASES = {
    "encrypt": "encrypt",
    "enc": "encrypt",
    "e": "encrypt",
    "decrypt": "decrypt",
    "dec": "decrypt",
    "d": "decrypt",
}


def parse_cipher_request(data: dict) -> dict:
    required_fields = ["cipher", "mode", "text"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    raw_cipher = data["cipher"].lower()
    cipher = CIPHER_ALIASES.get(raw_cipher)

    if not cipher:
        raise ValueError("Unsupported cipher. Type 'help' to see available options.")

    raw_mode = data["mode"].lower()
    mode = MODE_ALIASES.get(raw_mode)

    if not mode:
        raise ValueError("Mode must be encrypt/decrypt (e/d)")

    return {
        "cipher": cipher,
        "mode": mode,
        "text": data["text"],
        "params": data.get("params", {}),
    }


def parse_attack_request(data: dict) -> dict:
    if "attack" not in data or "text" not in data:
        raise ValueError("Attack request must contain 'attack' and 'text'")

    raw_attack = data["attack"].lower()
    attack = ATTACK_ALIASES.get(raw_attack)

    if not attack:
        raise ValueError("Unsupported attack. Type 'help' to see available options.")

    return {"attack": attack, "text": data["text"], "params": data.get("params", {})}
