# Import necessary libraries
import sys
import socket
from datetime import datetime
import time

# Define a function to scan ports
def scan_ports(target, start_port, end_port):
    # Print initial information about the scan
    print("="*50)
    print(f"Target: {target}")
    print(f"Start Port: {start_port}")
    print(f"End Port: {end_port}")
    print(f"Scan starting at: {datetime.now()}")
    print("="*50)

    try:
        # Create an empty list to store open ports
        openports = []
        # Loop through the range of ports
        for port in range(start_port, end_port + 1):
            # Create a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                # Set a timeout for the socket connection
                soc.settimeout(1)
                # Try to connect to the target on the current port
                print(f"Trying port {port}")
                result = soc.connect_ex((target, port))

                # If the connection is successful, the result will be 0
                if result == 0:
                    # Print the open port and add it to the list
                    print(f"\nOpen port: {port}\n")
                    openports.append(port)
                    # Sleep for a second to avoid overwhelming the target
                    time.sleep(0.5)
        # Print the list of open ports
        print(f"\nAll open ports: \n {openports}")

    # Handle exceptions
    except KeyboardInterrupt:
        # If the user interrupts the scan, exit the program
        print("\n Exiting...")
        sys.exit()

    except socket.gaierror:
        # If the hostname or IP address can't be resolved, exit the program
        print("Hostname/IP could not be resolved")
        sys.exit()

    except socket.error:
        # If there's a socket error, exit the program
        print("Could not connect to server")
        sys.exit()

# If the script is run directly (not imported as a module), execute the main function
if __name__ == "__main__":
    # Check if the user provided an IP address or hostname as an argument
    if len(sys.argv) == 4:
        # Resolve the IP address of the target
        target = socket.gethostbyname(sys.argv[1])
        # Extract the start and end port numbers from the arguments
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        # Start the port scan with the specified range of ports
        scan_ports(target, start_port, end_port)
    else:
        # If the user didn't provide the correct arguments, print an error message
        print("Invalid arguments \n Syntax: python3 port-scanner.py <ip> <start_port> <end_port>")
