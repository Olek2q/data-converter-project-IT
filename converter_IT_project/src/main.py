import argparse
from converter import convert_file


def main():
    parser = argparse.ArgumentParser(description='Konwerter plików')
    parser.add_argument('input', help='Plik wejściowy')
    parser.add_argument('output', help='Plik wyjściowy')
    args = parser.parse_args()

    convert_file(args.input, args.output)


if __name__ == "__main__":
    main()