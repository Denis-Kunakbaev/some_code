# Automated Tests for demoqa.com website

This project contains a set of automated tests for the [demoqa.com](https://demoqa.com/) website. Tests are written in Python using Selenium, PyTest, and webdriver-manager.

## Functionality

The project includes the following tests:

- **Web Tables Form Testing:**
    - Adding a new user to the table.
    - Checking the presence of a user in the table.
    - Deleting a new user from the table.
- **Browser Windows Form Testing:**
    - Opening a new tab.
    - Switching to a new tab.
    - Closing the current tab.
    - Navigating to the "Links" page.
    - Clicking the "Home" link.
    - Switching to a new tab.
    - Switching back to the original tab.
- **Alerts Form Testing:**
    - Opening alerts.
    - Get text from alerts.
    - Send text to alert.
- **Frame Form Testing:**
    - Opening frames form.
    - Switching between frames.

## Requirements

- Python 3.x
- Selenium
- PyTest
- webdriver-manager

## Installation

1. Clone the repository:

   git clone https://github.com/tquality-education-lvl1/d.kunakbaev.git


2. Install dependencies:
    pip install -r requirements.txt


3. Running Tests
    Run tests using pytest:
    pytest --browser Chrome or pytest --browser Firefox

## Project Structure
    Root
    ├── Elements
    │   ├── alert.py
    │   ├── base_element.py
    │   ├── button.py
    │   ├── frame.py
    │   ├── table.py
    │   ├── tabs.py
    │   └── text_field.py
    ├── Forms
    │   ├── alerts_form.py
    │   ├── base_form.py
    │   ├── browser_form.py
    │   ├── links_form.py
    │   └── webtables_form.py
    ├── Pages
    │   ├── base_page.py
    │   └── main_page.py
    ├── Tests
    │   ├── conftest.py
    │   └── test_demoqa.py
    └── Utils
        ├── browser_factory.py
        ├── json_helper.py
        ├── logger.py
        ├── singleton_driver.py
        ├── singleton_meta.py
        └── table_data_helper.py


Author
Denis-Kunakbaev