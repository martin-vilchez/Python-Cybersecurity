# Port Scanner

This repository hosts a Python-based port scanner designed as an educational tool for students exploring the fundamentals of cybersecurity. The script leverages Python's socket library to establish connections and identify open ports within a specified range. Each line of code is accompanied by a comment providing a brief explanation.

## How to Use

To utilize this port scanner, follow the steps outlined below:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Navigate to the Directory**: Use your terminal to navigate to the directory containing the script.
3. **Run the Script**: Execute the script using the following command:
   ```
   python3 port-scanner.py <ip> <start_port> <end_port>
   ```
   Replace `<ip>` with the IP address or hostname of the target you wish to scan. The script will scan ports starting from `<start_port>` through `<end_port>`, printing any open ports it discovers.

## Code Explanation

The port scanner script employs Python's `socket` library to attempt to establish a connection to each port on the target. If the connection is successful, the port is considered open. The socket library represents a Python-oriented interpretation of the Unix system call and library interface for sockets, providing a straightforward programming approach.

**Exception Handling**: The script includes exception handling to manage potential errors such as keyboard interrupts, hostname resolution issues, and socket errors.

## Disclaimer

Please note that this script is intended for educational purposes. Always ensure you have the necessary permissions before scanning IP addresses. Misuse of this tool is strictly discouraged.