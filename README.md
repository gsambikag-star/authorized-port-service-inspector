
# Authorized Local Port & Service Inspector

## Overview
A Python-based defensive network inspection tool designed to identify open TCP ports on the local machine.

## Objective
To inspect localhost (127.0.0.1) for open and closed ports using Python socket programming.

## Technologies Used
- Python
- Socket Programming
- TCP/IP
- Git and GitHub

## Features Implemented
- Localhost port scanning
- Single-port scanning
- Multiple-port scanning
- TCP socket connections
- Connection timeout configuration
- Open and closed port detection
- Standard service identification using port mappings
- Python dictionary-based service lookup
- Unknown service handling
- Formatted tabular terminal output

## Ports Tested
- 22 - SSH
- 80 - HTTP
- 443 - HTTPS
- 3306 - MySQL
- 8080 - Alternative HTTP

## Testing
Tested using a temporary local HTTP server.

Verified that port 8080 was detected as OPEN when the server was running and CLOSED after it was stopped.

## How to Run

1. Activate the virtual environment.
2. Execute:

python port_scanner.py

## Safety
The scanner is restricted to localhost (127.0.0.1).

## Project Status
Phase 1 - Project Setup Completed.

Phase 2 - Basic Port Scanning Completed.

Phase 3 - Service Identification Completed.

## Author 
Ambika G.S