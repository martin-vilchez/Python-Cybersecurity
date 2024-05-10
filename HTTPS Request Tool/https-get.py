import requests
import argparse

def parse_arguments():
    """
    Parse command-line arguments for the HTTPS request tool.
    Make help statements
    """
    parser = argparse.ArgumentParser(description='HTTPS Request Tool')

    # Required argument for the URL
    parser.add_argument('url', help='Target URL for the HTTPS request')

    # Optional request configuration flags
    parser.add_argument('-H', '--header', action='append', help='Custom headers for the request')
    parser.add_argument('-C', '--cookie', action='append', help='Custom cookies for the request')
    parser.add_argument('-x', '--proxy', help='Proxy for the request')
    parser.add_argument('-a', '--auth', help='Authentication credentials in the format "username:password"')

    return parser.parse_args()

def send_request(args):
    """
    Send a GET request with the specified URL and optional request configuration.
    """
    request_headers = dict(header.split(':') for header in args.header) if args.header else None
    request_cookies = dict(cookie.split('=') for cookie in args.cookie) if args.cookie else None
    auth = tuple(args.auth.split(':')) if args.auth else None
    proxies = {'http': args.proxy, 'https': args.proxy} if args.proxy else None

    return requests.get(args.url, headers=request_headers, cookies=request_cookies, proxies=proxies, auth=auth)

def print_response(args, response):
    """
    Print the status code and content of the response.
    """
    print(f"\nURL: {args.url}\n{'='*50}")
    if args.cookie:
        print(f"Cookies: {dict(cookie.split('=') for cookie in args.cookie)}\n{'='*50}")
    if args.header:
        print(f"Headers:\n {dict(header.split(':') for header in args.header)}\n{'='*50}")
    print(f"Status Code: {response.status_code}\n{'='*50}")
    print(f"Response Content: {response.content.decode()}\n{'='*50}")

def main():
    args = parse_arguments()
    response = send_request(args)
    print_response(args, response)

if __name__ == "__main__":
    main()
