
import socket

# Target computer
target = "127.0.0.1"

# List of ports to scan
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

print("Starting Port Scanner...")
print("Target:", target)
print("-" * 55)

# Scan each port
for port in ports:

    # Get service name
    service = services.get(port, "Unknown")

    try:
        # Create socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            # Set timeout
            s.settimeout(1)

            # Attempt connection
            s.connect((target, port))

            # Connection successful
            status = "OPEN"

    except ConnectionRefusedError:
        status = "CLOSED"

    except socket.timeout:
        status = "TIMEOUT"

    except OSError as error:
        status = f"ERROR ({error})"

    # Display results
    print(f"Port {port:<5} | {service:<10} | {status}")

print("-" * 55)
print("Port scanning completed!")
