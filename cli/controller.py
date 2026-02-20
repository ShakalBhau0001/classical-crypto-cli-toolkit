from core.ciphers import caesar, playfair, rail_fence, row_column
from core.attacks import caesar_brute, rail_fence_brute


def handle_cipher(request: dict):
    cipher = request["cipher"]
    mode = request["mode"]
    text = request["text"]
    params = request["params"]

    if cipher == "caesar":
        shift = params.get("shift")
        if shift is None:
            raise ValueError("Caesar cipher requires 'shift'")

        if mode == "encrypt":
            return caesar.encrypt(text, shift)
        return caesar.decrypt(text, shift)

    elif cipher == "playfair":
        keyword = params.get("keyword")
        merge_letter = params.get("merge_letter", "I")

        if keyword is None:
            raise ValueError("Playfair requires 'keyword'")

        if mode == "encrypt":
            return playfair.encrypt(text, keyword, merge_letter)
        return playfair.decrypt(text, keyword, merge_letter)

    elif cipher == "rail_fence":
        rails = params.get("rails")
        if rails is None:
            raise ValueError("Rail Fence requires 'rails'")

        if mode == "encrypt":
            return rail_fence.encrypt(text, rails)
        return rail_fence.decrypt(text, rails)

    elif cipher == "row_column":
        key = params.get("key")
        if key is None:
            raise ValueError("Row-Column requires 'key'")

        if mode == "encrypt":
            return row_column.encrypt(text, key)
        return row_column.decrypt(text, key)

    else:
        raise ValueError("Unsupported cipher")


def handle_attack(request: dict):
    attack = request["attack"]
    text = request["text"]
    params = request["params"]

    if attack == "caesar":
        return caesar_brute.brute_force(text)

    elif attack == "rail_fence":
        max_rails = params.get("max_rails")
        return rail_fence_brute.brute_force(text, max_rails)

    else:
        raise ValueError("Unsupported attack")
