
import socket

# Target computer
target = "127.0.0.1"

# List of ports to scan
ports = [22, 80, 443, 3306, 8080]

print("Starting Port Scanner...")
print("Target:", target)
print("-" * 35)

# Scan each port
for port in ports:

    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set timeout
    s.settimeout(1)

    # Try connecting to the port
    result = s.connect_ex((target, port))

    # Display result
    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    # Close socket
    s.close()

print("-" * 35)
print("Port scanning completed!")
