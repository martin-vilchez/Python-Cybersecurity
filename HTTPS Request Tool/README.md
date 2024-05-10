# HTTPS Request Tool

This repository contains a Python script designed to teach the fundamentals of cybersecurity by demonstrating how to send HTTPS requests and analyze the responses. The script uses the `requests` and `argparse` libraries to send GET requests to a specified URL with optional request configurations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

**Prerequisites:** Python 3.x, request library & argpase library

1. Clone the repository:
   ```
   git clone https://github.com/martin-vilchez/Python-Cybersecurity.git
   ```
2. Navigate to the cloned repository:
   ```
   cd https-request-tool
   ```
3. Change permissions:
   ```
   Chmod +x https-get.py 
   ```
4. Ready to run!

## Usage

The script can be run from the command line with the following syntax:

```
python3 https-getl.py <url> [options]
```

**Arguments:**

- `<url>`: The target URL for the HTTPS request. This argument is required.
- `-H, --header`: Custom headers for the request. This argument is optional and can be used multiple times.
- `-C, --cookie`: Custom cookies for the request. This argument is optional and can be used multiple times.
- `-x, --proxy`: Proxy for the request. This argument is optional.
- `-a, --auth`: Authentication credentials in the format "username:password". This argument is optional.

**Example:**

```
python https-get.py https://example.com -H "User-Agent: MyUserAgent" -C "sessionid=1234567890" -x "http://myproxy:8080" -a "username:password"
```

This command sends a GET request to `https://example.com` with a custom User-Agent header, a custom sessionid cookie, a proxy, and authentication credentials.

