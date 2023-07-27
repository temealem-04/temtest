��#   t e m t e s t 
 
 Step 1: Install prerequisites

Install Python: Download and install Python from the official website (https://www.python.org/) if you haven't already.
Install pytest: Open your terminal or command prompt and run pip install pytest to install pytest.
Install Selenium: Run pip install selenium to install the Selenium WebDriver library.
Step 2: Set up the project structure
Create a new directory for your test framework and set up the project structure with the following directories and files:

lua
Copy code
my_test_framework/
|-- tests/
|   |-- test_sample.py
|-- pages/
|   |-- base_page.py
|-- utilities/
|   |-- config.py
|   |-- logger.py
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
Step 3: Write test cases
In the tests directory, create a new file named test_sample.py (you can use any name you prefer) and write your test cases using pytest conventions. For example:

python
Copy code
import pytest

@pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
def test_greet_name(name):
    # Your test code here
    assert True
Step 4: Implement page objects
In the pages directory, create a file named base_page.py or any other relevant page object files. Implement the page object pattern to represent web pages and encapsulate interactions with them. For example:

python
Copy code
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

    def find_element(self, by, value):
        return self.driver.find_element(by, value)
Step 5: Set up pytest fixtures
In the conftest.py file, define pytest fixtures that provide the WebDriver instance and other commonly used setups. For example:

python
Copy code
import pytest
from selenium import webdriver
from pages.base_page import BasePage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # You can use other browsers as well
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def base_page(driver):
    return BasePage(driver)
Step 6: Configure pytest
Create a pytest.ini file in the project root directory to configure pytest settings. For example:

ini
Copy code
[pytest]
addopts = -vs
testpaths = tests
Step 7: Create a Docker Compose file
Create a new file named docker-compose.yml in your project directory and define the services for Selenium Grid hub and Chrome node. For example:

yaml
Copy code
version: '3'
services:
  selenium-hub:
    image: selenium/hub:latest
    ports:
      - "4444:4444"
    networks:
      - selenium-network

  chrome-node:
    image: selenium/node-chrome:latest
    depends_on:
      - selenium-hub
    environment:
      - HUB_HOST=selenium-hub
      - HUB_PORT=4444
    networks:
      - selenium-network

networks:
  selenium-network:
Step 8: Save the docker-compose.yml file and navigate to the project directory in your terminal or command prompt.

Step 9: Start the services
Run the following command to start the services defined in the Docker Compose file:

Copy code
docker-compose up -d
Step 10: Verify the setup
After the containers are running, visit http://localhost:4444/grid/console in your web browser to verify the Selenium Grid console.

Step 11: Run your tests
In your test automation code (e.g., test_sample.py), use the Selenium Grid's hub URL (http://localhost:4444/wd/hub) as the remote WebDriver URL to connect to the Chrome node and execute tests. For example:

python
Copy code
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    grid_url = "http://localhost:4444/wd/hub"
    capabilities = {"browserName": "chrome"}
    driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_greet_name(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
Step 12: Stop the services
To stop and remove the containers created by Docker Compose, run the following command:

Copy code
docker-compose down
That's it! You now have a test automation framework using Python with pytest and Selenium, running tests on a Dockerized Selenium Grid.
