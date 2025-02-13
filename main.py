import argparse
from modules import port_scanner, brute_forcer, http_server_scanner

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument("--scan", help="Scan ports of a target", nargs='*')
    parser.add_argument("--brute", help="Brute force password list on a target", nargs='*')
    parser.add_argument("--http-scan", help="Scan HTTP server paths on a target", nargs='*')
    args = parser.parse_args()

    if args.scan:
        target = args.scan[0]
        ports = list(map(int, args.scan[1:]))
        open_ports = port_scanner.scan_ports(target, ports)
        print(f"Open Ports on {target}: {open_ports}")

    if args.brute:
        target = args.brute[0]
        username = args.brute[1]
        password_list = args.brute[2:]
        valid_password = brute_forcer.brute_force(password_list, target, username, brute_forcer.validate_http_basic_auth)
        if valid_password:
            print(f"Password found for {username}: {valid_password}")
        else:
            print(f"No valid password found for {username}.")

    if args.http_scan:
        target = args.http_scan[0]
        paths = args.http_scan[1:]
        available_paths = http_server_scanner.scan_http_server(target, paths)
        print(f"Available paths on {target}: {available_paths}")

if __name__ == "__main__":
    main()
