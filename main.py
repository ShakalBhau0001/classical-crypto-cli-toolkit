import argparse
from cli.parser import parse_cipher_request, parse_attack_request
from cli.controller import handle_cipher, handle_attack

# User-friendly short commands
CIPHER_ALIASES = {
    "c": "caesar",
    "pf": "playfair",
    "rf": "rail_fence",
    "rail": "rail_fence",
    "rc": "row_column",
    "row": "row_column",
}

ATTACK_ALIASES = {
    "c": "caesar",
    "rf": "rail_fence",
}


def normalize_cipher(name):
    return CIPHER_ALIASES.get(name, name)


def normalize_attack(name):
    return ATTACK_ALIASES.get(name, name)


# Cipher Execution
def run_cipher(args):
    cipher_name = normalize_cipher(args.cipher)

    if not (args.encrypt or args.decrypt):
        raise ValueError("You must specify either --encrypt or --decrypt.")

    mode = "encrypt" if args.encrypt else "decrypt"

    # Mapping correct key/keyword for Playfair & Row-Column
    params = vars(args).copy()
    if cipher_name == "playfair":
        if not getattr(args, "keyword", None):
            raise ValueError("Playfair requires 'keyword' / key")
        # Backend expects 'keyword', user may provide -k or --keyword
        params["keyword"] = args.keyword
    elif cipher_name == "row_column":
        if not getattr(args, "keyword", None):
            raise ValueError("Row-Column requires 'keyword'")
        # Backend expects 'key', user may provide -k or --keyword
        params["key"] = args.keyword

    request = parse_cipher_request(
        {
            "cipher": cipher_name,
            "mode": mode,
            "text": args.text,
            "params": params,
        }
    )

    result = handle_cipher(request)
    print(result)


# Attack Execution
def run_attack(args):
    attack_name = normalize_attack(args.attack_type)

    request = parse_attack_request(
        {
            "attack": attack_name,
            "text": args.text,
            "params": vars(args),
        }
    )

    result = handle_attack(request)

    if attack_name == "caesar":
        for entry in result:
            print(f"Shift {entry['shift']:2} → {entry['plaintext']}")

    elif attack_name == "rail_fence":
        for entry in result:
            print(f"Rails {entry['rails']:2} → {entry['plaintext']}")


# CLI Setup
def main():
    parser = argparse.ArgumentParser(description="Classical Cryptography CLI Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # Help Subcommand
    help_parser = subparsers.add_parser("help", aliases=["h"], help="Show help message")
    help_parser.set_defaults(func=lambda args: parser.print_help())

    #  Caesar Cipher
    caesar_parser = subparsers.add_parser("caesar", aliases=["c"], help="Caesar cipher")
    mode_group = caesar_parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("-e", "--encrypt", action="store_true")
    mode_group.add_argument("-d", "--decrypt", action="store_true")
    caesar_parser.add_argument("text", help="Input text")
    caesar_parser.add_argument("-s", "--shift", type=int, required=True)
    caesar_parser.set_defaults(func=run_cipher, cipher="caesar")

    #  Playfair Cipher
    playfair_parser = subparsers.add_parser(
        "playfair", aliases=["pf"], help="Playfair cipher"
    )
    mode_group = playfair_parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("-e", "--encrypt", action="store_true")
    mode_group.add_argument("-d", "--decrypt", action="store_true")
    playfair_parser.add_argument("text", help="Input text")
    # User can pass -k, --keyword, or --key for Playfair
    playfair_parser.add_argument(
        "-k", "--keyword", "--key", dest="keyword", required=True
    )
    playfair_parser.set_defaults(func=run_cipher, cipher="playfair")

    #  Rail Fence Cipher
    rail_parser = subparsers.add_parser(
        "rail_fence", aliases=["rf", "rail"], help="Rail Fence cipher"
    )
    mode_group = rail_parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("-e", "--encrypt", action="store_true")
    mode_group.add_argument("-d", "--decrypt", action="store_true")
    rail_parser.add_argument("text", help="Input text")
    rail_parser.add_argument("-r", "--rails", type=int, required=True)
    rail_parser.set_defaults(func=run_cipher, cipher="rail_fence")

    #  Row Column Cipher
    row_parser = subparsers.add_parser(
        "row_column", aliases=["rc", "row"], help="Row Column cipher"
    )
    mode_group = row_parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("-e", "--encrypt", action="store_true")
    mode_group.add_argument("-d", "--decrypt", action="store_true")
    row_parser.add_argument("text", help="Input text")
    # User can pass -k, --keyword, or --key for Row-Column
    row_parser.add_argument("-k", "--keyword", "--key", dest="keyword", required=True)
    row_parser.set_defaults(func=run_cipher, cipher="row_column")

    #  Attack Subcommands
    attack_parser = subparsers.add_parser(
        "attack", aliases=["atk"], help="Cipher attacks"
    )
    attack_parser.add_argument(
        "attack_type", choices=["caesar", "c", "rail_fence", "rf"], help="Attack type"
    )
    attack_parser.add_argument("text", help="Ciphertext")
    attack_parser.add_argument("--max-rails", type=int)
    attack_parser.set_defaults(func=run_attack)

    args = parser.parse_args()

    # Executing selected command
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
