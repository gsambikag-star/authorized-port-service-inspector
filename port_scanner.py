import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

# Safety restriction: localhost only
TARGET = "127.0.0.1"

# Default ports
DEFAULT_PORTS = [22, 80, 443, 3306, 8080]

# Common service names
services = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}


# Convert user input into a list of valid ports
def parse_ports(port_input):
    selected_ports = set()

    try:
        for part in port_input.split(","):
            part = part.strip()

            if not part:
                raise ValueError

            if "-" in part:
                start, end = map(int, part.split("-"))

                if not (1 <= start <= end <= 65535):
                    raise ValueError

                selected_ports.update(range(start, end + 1))

            else:
                port = int(part)

                if not 1 <= port <= 65535:
                    raise ValueError

                selected_ports.add(port)

    except ValueError:
        raise argparse.ArgumentTypeError(
            "Enter valid ports, e.g. 80,443 or 1-100"
        )

    if not selected_ports:
        raise argparse.ArgumentTypeError("At least one port is required")

    return sorted(selected_ports)


# Read command-line arguments
parser = argparse.ArgumentParser(
    description="Authorized Local Port & Service Inspector"
)

parser.add_argument(
    "--ports",
    type=parse_ports,
    default=DEFAULT_PORTS,
    help="Ports or port ranges to scan (example: 80,443 or 1-100)"
)

args = parser.parse_args()
ports = args.ports


# Scan one port
def scan_port(port):
    service = services.get(port, "Unknown")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((TARGET, port))
            status = "OPEN"

    except ConnectionRefusedError:
        status = "CLOSED"

    except socket.timeout:
        status = "TIMEOUT"

    except OSError as error:
        status = f"ERROR ({error})"

    return port, "TCP", service, status


# Display results in a table
print("\nAuthorized Local Port & Service Inspector")
print("Target:", TARGET)
print("Ports selected:", len(ports))
print("-" * 65)

print(f"{'PORT':<10}{'PROTOCOL':<12}{'SERVICE':<15}{'STATUS'}")
print("-" * 65)

with ThreadPoolExecutor(max_workers=min(5, len(ports))) as executor:
    results = list(executor.map(scan_port, ports))

for port, protocol, service, status in results:
    print(f"{port:<10}{protocol:<12}{service:<15}{status}")

print("-" * 65)

# Display open ports
open_ports = [result[0] for result in results if result[3] == "OPEN"]

print("\nOPEN PORT SUMMARY")

if open_ports:
    for port in open_ports:
        print(f"Port {port} is OPEN")
else:
    print("No open ports detected.")

print("\nPort scanning completed!")
