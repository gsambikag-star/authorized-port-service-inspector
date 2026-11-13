from concurrent.futures import ThreadPoolExecutor

import socket
from concurrent.futures import ThreadPoolExecutor

# Target computer (localhost only)
target = "127.0.0.1"

# Ports to scan
ports = [22, 80, 443, 3306, 8080]

# Service identification
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


# Function to scan an individual port
def scan_port(port):

    service = services.get(port, "Unknown")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            # Set timeout
            s.settimeout(1)

            # Attempt connection
            s.connect((target, port))

            status = "OPEN"

    except ConnectionRefusedError:
        status = "CLOSED"

    except socket.timeout:
        status = "TIMEOUT"

    except OSError as error:
        status = f"ERROR ({error})"

    return port, service, status


print("Starting Multithreaded Port Scanner...")
print("Target:", target)
print("-" * 60)

# Create a thread pool
with ThreadPoolExecutor(max_workers=5) as executor:

    # Scan multiple ports concurrently
    results = executor.map(scan_port, ports)

    # Display results
    for port, service, status in results:
        print(f"Port {port:<5} | {service:<10} | {status}")

print("-" * 60)
print("Port scanning completed!")
