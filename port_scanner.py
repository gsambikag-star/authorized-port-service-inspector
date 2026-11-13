
import socket

# Target computer
target = "127.0.0.1"

# List of ports to scan
ports = [22, 80, 443, 3306, 8080]

# Dictionary containing service names
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
print("-" * 50)

# Scan each port
for port in ports:

    # Get the service name
    service = services.get(port, "Unknown")

    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set timeout
    s.settimeout(1)

    # Try connecting to the port
    result = s.connect_ex((target, port))

    # Display port, service and status
    if result == 0:
        status = "OPEN"
    else:
        status = "CLOSED"

    print(f"Port {port:<5} | {service:<10} | {status}")

    # Close socket
    s.close()

print("-" * 50)
print("Port scanning completed!")
