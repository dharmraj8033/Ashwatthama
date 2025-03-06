import argparse
from scanner.scanner import Scanner
from scanner.payload_manager import PayloadManager

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--params", required=True, help="Comma-separated parameters")
    args = parser.parse_args()

    payload_manager = PayloadManager("payloads/")
    scanner = Scanner(args.url, args.params.split(","), payload_manager)
    results = scanner.run_scan()
    print(results)

if __name__ == "__main__":
    main()