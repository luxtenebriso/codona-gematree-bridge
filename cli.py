import argparse
from gematree_to_codona import generate_codona_capsule

def main():
    parser = argparse.ArgumentParser(description="Generate Codona capsule from phrase using gematria logic")
    parser.add_argument("phrase", help="Input phrase to encode (e.g. 'Amrita')")
    args = parser.parse_args()
    generate_codona_capsule(args.phrase)

if __name__ == "__main__":
    main()
