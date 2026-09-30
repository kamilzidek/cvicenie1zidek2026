"""A small command-line greeting application."""

import argparse


def greeting(name: str = "svet") -> str:
    """Return a greeting for *name*."""
    return f"Ahoj, {name}!"


def main() -> None:
    """Run the greeting application."""
    parser = argparse.ArgumentParser(description="Pozdrav z mojej prvej Python aplikácie.")
    parser.add_argument("name", nargs="?", default="svet", help="Meno, ktoré má aplikácia pozdraviť.")
    args = parser.parse_args()
    print(greeting(args.name))


if __name__ == "__main__":
    main()
