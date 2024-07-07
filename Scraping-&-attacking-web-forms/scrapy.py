import argparse
import requests
from bs4 import BeautifulSoup


def parse_form(url):
    """Fetches the form data from the given URL and returns the parsed payload.

    Args:
        url (str): The URL of the web page containing the form.

    Returns:
        dict: A dictionary containing the form data with field names as keys and their
              corresponding values or empty strings (for missing values) as values.

    Raises:
        ValueError: If the HTTP response status code is not 200 (successful).
    """

    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')

    form = soup.find('form')
    if not form:
        raise ValueError("Form not found in the provided URL.")

    action = form.get('action')
    method = form.get('method', 'POST').upper()  # Default to POST if unspecified

    payload = {}
    for input_field in form.find_all('input'):
        name = input_field.get('name')
        input_type = input_field.get('type')
        value = input_field.get('value', '')

        if name:
            payload[name] = input(f"Enter a value for input field {name}: ")
    
    return payload, action, method


def submit_form(url, payload, method='POST'):
    """Submits the form data to the specified URL using the provided method.

    Args:
        url (str): The URL of the web page containing the form.
        payload (dict): A dictionary containing the form data.
        method (str, optional): The HTTP method to use for submission. Defaults to 'POST'.

    Returns:
        requests.Response: The response object from the form submission request.
    """

    response = requests.request(method, url, data=payload)
    return response


def main():
    """Parses command-line arguments and handles form submission."""

    parser = argparse.ArgumentParser(description="Form submission script")
    parser.add_argument('url', help="The URL of the web page containing the form")
    args = parser.parse_args()

    try:
        payload, action, method = parse_form(args.url)
        print("Form data parsed successfully:", payload)
        response = submit_form(args.url + action, payload, method.lower())

        if response.status_code == 200:
            print("Form submitted successfully.")
        else:
            print(f"Error submitting form: {response.status_code}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()