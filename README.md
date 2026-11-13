# Authorized Local Port & Service Inspector

## 1. Overview

A Python-based defensive network inspection tool designed to identify open TCP ports and common services running on the local machine.

## 2. Objective

To inspect localhost (`127.0.0.1`) for open TCP ports using Python socket programming, identify commonly associated services, and display scan results in a structured table.

## 3. Technologies Used

- Python
- Socket Programming
- TCP/IP Networking
- `concurrent.futures`
- `ThreadPoolExecutor`
- `argparse`
- Git and GitHub

## 4. Features Implemented

- Localhost-only TCP port scanning
- Single-port and multiple-port scanning
- User-configurable port selection and ranges
- TCP socket connections
- Connection timeout configuration
- Open, closed, timeout and error status detection
- Standard service identification using port mappings
- Dictionary-based service lookup
- Unknown service handling
- Multithreaded scanning using `ThreadPoolExecutor`
- Concurrent scanning with up to 5 worker threads
- Formatted tabular terminal output
- Summary of detected open ports
- Exception handling using `try-except`
- Connection refused detection
- Graceful handling of socket errors
- Automatic socket resource cleanup

## 5. Ports and Services

The default ports configured for scanning are:

| Port | Service |
|---|---|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 8080 | Alternative HTTP |

Additional ports are identified as `Unknown` if they are not included in the service mapping.

## 6. How to Run

### Step 1: Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 2: Run the default scan

```bash
python port_scanner.py
```

### Step 3: Scan selected ports

```bash
python port_scanner.py --ports 80,443,8080
```

### Step 4: Scan a port range

```bash
python port_scanner.py --ports 1-100
```

### Step 5: Display help

```bash
python port_scanner.py --help
```

## 7. Sample Terminal Output

The following is an example of a successful scan when a local HTTP server is running on port 8080.

```text
Authorized Local Port & Service Inspector
Target: 127.0.0.1
Ports selected: 1

PORT      PROTOCOL    SERVICE        STATUS
-----------------------------------------------------------------
8080      TCP         HTTP-ALT       OPEN
-----------------------------------------------------------------

OPEN PORT SUMMARY
Port 8080 is OPEN

Port scanning completed!
```

## 8. Testing Performed

| Test Case | Expected Result | Status |
|---|---|---|
| Default port scanning | Display scan results | Passed |
| Selected-port scanning | Scan specified ports | Passed |
| Port-range scanning | Scan all ports in range | Passed |
| Local HTTP server running | Port 8080 shows OPEN | Passed |
| Local HTTP server stopped | Port 8080 shows CLOSED or TIMEOUT | Passed |
| Invalid port number (700000) | Reject input | Passed |
| Non-numeric input (abc) | Reject input | Passed |
| Invalid port range (100-50) | Reject input | Passed |
| Help command | Display usage instructions | Passed |
| Localhost-only configuration | No target argument exposed | Passed |

## 9. Understanding Port Status

- **OPEN:** A service accepted the TCP connection.
- **CLOSED:** The connection was actively refused.
- **TIMEOUT:** No response was received within the configured timeout.
- **ERROR:** Another socket-related error occurred.

A timeout does not necessarily mean that a port is closed.

## 10. Safety Restrictions

- The scanner is configured to target localhost (`127.0.0.1`) only.
- The target address is hardcoded in the Python program.
- No command-line option is provided to specify external IP addresses or domains.
- Only valid TCP port numbers between 1 and 65535 are accepted.
- Invalid port inputs and ranges are rejected.
- The tool is intended for authorized defensive testing.
- Use scanning tools only on systems you own or have explicit permission to inspect.

## 11. Project Status

- Phase 1 – Project Setup and GitHub Initialization: Completed
- Phase 2 – Basic TCP Port Scanning: Completed
- Phase 3 – Service Identification: Completed
- Phase 4 – Timeout and Error Handling: Completed
- Phase 5 – Multithreaded Port Scanning: Completed
- Phase 6 – Final Output and Documentation: Completed

## 12. Project Outcome

Successfully developed a multithreaded local TCP port and service inspector using Python.

The project supports configurable port selection, port-range scanning, service identification, timeout and error handling, tabular results, and localhost-only scanning.

## Author

**Ambika G.S**
