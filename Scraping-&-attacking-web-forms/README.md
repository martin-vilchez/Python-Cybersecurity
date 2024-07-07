# Scraping & attacking web forms

This repository contains a Python script designed to automate form submission on web pages. It is intended for educational purposes within the context of a cybersecurity and Python fundamentals.

**Functionality:**

* Fetches a web page's form data using Beautiful Soup for HTML parsing.
* Prompts the user to enter values for each form field.
* Submits the form data to the target URL.
* Provides feedback on successful or failed form submission, including the HTTP status code.

**Learning Objectives:**

* Explore the functionalities of libraries like `requests` and `BeautifulSoup`.
* Learn about common form submission methods (POST/GET).
* Practice user input handling in Python scripts.
* Security implications of form submission automation.

**Getting Started:**

1. **Prerequisites:**
    * Python 3 (download from [https://www.python.org/downloads/](https://www.python.org/downloads/))
    * pip (package installer for Python) - usually comes bundled with Python
2. **Installation:**
    * Clone this repository: `git clone https://<your_repository_url>`
    * Navigate to the project directory: `cd python-form-submission`
    * Install required libraries: `pip install requests beautifulsoup4`
3. **Usage:**
    * Open a terminal in the project directory.
    * Run the script with the URL of the web page containing the form:
        ```bash
        python scrapy.py https://www.url-with-form.com/index.html
        ```
    * The script will prompt you for each form field value. Enter the desired data and press Enter.
    * Upon submission, the script will display a success message or an error code if unsuccessful.

**Important Notes:**

* The script assumes the form is a simple HTML form and might not work for complex forms with JavaScript or other advanced features.
* Be aware of potential security risks when automating form submissions, especially on untrusted websites.

**Further Exploration:**

* Explore parsing different form field types (text boxes, dropdowns, checkboxes).
* Modify the script to handle hidden form fields or additional submission methods.
* Learn about advanced web scraping techniques with libraries like Selenium.

**Happy Learning!**

This READEME provides a comprehensive overview of the Python form submission script and its educational value within a cybersecurity and Python fundamentals course. Feel free to modify this template as needed for your specific case.
