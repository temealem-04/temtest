# FiscalNote Automated Functional Testing
1. [Required Software](#required-software)
2. [Initial Set Up](#initial-set-up)
3. [Selenium Grid](#selenium-grid)
4. [Executing Tests](#executing-tests)
5. [Watching Test Runs](#watching-test-runs)
6. [Contributing](#contributing)
7. [Learning Resources](#learning-resources)

## Required Software
* [Docker](https://docs.docker.com/install/)
* [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
* [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)

## Initial Set Up
### Clone the Repository
Via HTTPS: `git clone https://github.com/FiscalNote/fn_aft.git`

Via SSH: `git clone git@github.com:FiscalNote/fn_aft.git`

### Install the Project's Dependencies
Change into the project folder:

`cd /path/to/fn_aft`

Begin by setting up a [Virtual Environment](https://docs.python.org/3.7/tutorial/venv.html) in the project root:

`python3 -m venv venv`

Next, activate your virtual environment:

`source venv/bin/activate`

Install all the dependencies from the [requirements.txt]() file:

`pip install -r requirements.txt`

## Selenium Grid
We run all of our tests through an instance of [Selenium Grid](https://www.selenium.dev/documentation/en/grid/).

### Setting Up Selenium Grid
Our [docker-compose.yml](https://github.com/FiscalNote/fn_aft/blob/master/docker-compose.yml) file contains a basic
configuration for an instance of Selenium Grid that contains 1 Chrome browser and 1 Firefox browser.

Execute the following command to spin up Selenium Grid Docker containers:

`docker-compose up -d`

After Docker finishes running, you can verify the the setup was successful by navigating to:

[http://localhost:4444/grid/console](http://localhost:4444/grid/console)

### Tearing Down Selenium Grid
Execute the following command to tear down the Selenium Grid Docker containers:

`docker-compose down`

## Executing Tests
__A Word of Warning:__ Many of the tests in this framework are highly destructive with respect to bulk deletion of data
before and after test suites run. This gives our test suites a pristine environment for test case execution. You should
avoid running any of the test suites in this Framework with a user in the main FiscalNote organization. Instead, you
should set up a new test organization with new test users to execute test suites. If you do not know what this means,
you should reach out to someone on the Quality Assurance team before executing any test suites in this framework.

With that out of the way, all tests execute in the `staging` environment by default. This can be modified with the
`--environment` flag:

* __dev:__ `--environment development`
* __staging:__ `--environment staging`
* __app:__ `--environment production` 

All tests will also run against Chrome on the local Selenium Grid by default. This can be modified with the `--browser` 
flag. The following browsers are available locally:

* __Chrome:__: `--browser chrome`
* __Firefox__: `--browser firefox`

Alternatively, you can run tests against BrowserStack with the following flags:

* __Chrome:__: `--browser chrome-bs`
* __Firefox__: `--browser firefox-bs`
* __Internet Explorer__: `--browser internet-explorer-bs`
* __Safari__: `--browser safari-bs`

A full command for running the login test suite locally against Firefox on production is below:

`pytest -m login --environment production --browser firefox`

The corresponding command for BrowserStack would would be:

`pytest -m login --environment production --browser firefox-bs`

If you receive an authentication error, you should review the BrowserStack configuration section above.

### Required Environment Variables
This framework expects the `ENV_PASSWORD` and `ENV_USERNAME` environment variables to contain the password and username
of a valid FiscalNote account. In order to use the framework, set these variables:

```.env
export ENV_PASSWORD=password_goes_here
export ENV_USERNAME=username_goes_here
```

### Optional Environment Variables
If you plan to execute tests against [BrowserStack](https://www.browserstack.com/automate), you must set the 
`ENV_BS_PASSWORD` and `ENV_BS_USERNAME` environment variables to contain the password and username for your
BrowserStack account. You can find your credentials in [Account Settings](https://www.browserstack.com/accounts/settings)
on BrowserStack.

```.env
export ENV_BS_PASSWORD=password_goes_here
export ENV_BS_USERNAME=username_goes_here
```

### Additional BrowserStack Configuration
There is one additional environment variable that needs to be set in order to properly annotate tests within the
BrowserStack user interface:

* `ENV_BS_TEST_SUITE_NAME`: The name of your test suite--for instance, "Schedules Custom Query."

### Example Commands
A complete command that runs login tests against staging using Firefox the local Selenium Grid is below:

`pytest -m login --environment staging --browser firefox`

A complete command that runs login tests against development using Internet Explorer on BrowserStack is below:

`pytest -m login --environment dev --browser internet-explorer-bs`

### Deep Links
`pytest -m deep_links`

### Directory
`pytest -m directory`

### Discovery Alerts - CRUD
`pytest -m bill_discovery_alerts_crud`

`pytest -m crs_report_discovery_alerts_crud`

`pytest -m federal_regulation_discovery_alerts_crud`

`pytest -m international_bill_discovery_alerts_crud`

`pytest -m international_regulation_discovery_alerts_crud`

`pytest -m puc_ferc_discovery_alerts_crud`

`pytest -m state_regulation_discovery_alerts_crud`

### Discovery Alerts - Populated
`pytest -m populated_bill_discovery_alert`

`pytest -m populated_crs_report_discovery_alert`

`pytest -m populated_federal_regulation_discovery_alert`

`pytest -m populated_public_inspection_desk_discovery_alert`

`pytest -m populated_state_regulation_discovery_alert`

### Drive - Files
`pytest -m drive_files`

### Drive - Links
`pytest -m drive_links`

### Entity Page - State Regulations
`pytest -m state_regulations_entity_page`

### Forgot Password
`pytest -m forgot_password`

### Issue Actions Tab
`pytest -m issue_actions_tab`

### Issue Brief
`pytest -m issue_brief`

### Issue Files Tab
`pytest -m issue_files_tab`

### Issue Links Tab
`pytest -m issue_links_tab`

### Issue Overview Tab
`pytest -m issue_overview_tab`

### Issue Stakeholders Tab
`pytest -m issue_stakeholders_tab`

### Issues List
`pytest -m issues`

### Mailing Lists
`pytest -m mailing_list`

### Navigation
`pytest -m navigation`

### Search
`pytest -m search`

### Social Media Monitoring
`pytest -m social_media_monitoring`

### Standard Login
`pytest -m login`

### SSO Login
`pytest -m sso_login`

## Watching Test Runs
It can be useful to watch a test suite as it executes, particularly when writing a new test suite or diagnosing a test
suite failure. This is the primary use of [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/).

The sections below show the required settings for viewing tests running through Chrome and Firefox. If prompted, the
password for the virtual machine is `secret`.

### Chrome VNC Viewer Settings
![Chrome VNC Viewer Settings](https://github.com/FiscalNote/fn_aft/blob/master/vnc_viewer_chrome.png)

### Firefox VNC Viewer Settings
![Firefox VNC Viewer Settings](https://github.com/FiscalNote/fn_aft/blob/master/vnc_viewer_firefox.png)

## Contributing
All contributions to this repository must be linked to a ticket from the [FNAT Backlog](https://fiscalnote2.atlassian.net/secure/RapidBoard.jspa?rapidView=122&view=planning.nodetail&issueLimit=100).

### Pull Request Process
To make contributions to this codebase, please create a fork of this repository and submit all suggested changes
 through a pull request.

Before submitting a pull request, please ensure:

* Configure your new test suite to pass in the development, staging, and production environment.
* Ensure that your new test suite did not break any other test suites. Yes, you must run all of the tests in the
[Executing Tests](#executing-tests)) section before your pull request will be merged.
* Document any new test execution commands in the [Executing Tests](#executing-tests)) section.

Please assign the pull request to one of the [contributors](https://github.com/fn-marc-clinedinst/fn_aft/graphs/contributors),
who will review and merge the pull request when it is ready.

## Learning Resources
### Python Resources
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [Dive into Python 3](https://diveintopython3.problemsolving.io/)
* [How to Think Like a Computer Scientist](https://runestone.academy/runestone/books/published/thinkcspy/index.html)
* [Official pytest Documentation](https://docs.pytest.org/en/latest/)
* [Official Python Tutorial](https://docs.python.org/3.7/tutorial/)

### Selenium Resources
* [Distributed Testing with Selenium Grid and Docker](https://testdriven.io/blog/distributed-testing-with-selenium-grid/)
* [Selenium Python Documentation](https://selenium-python.readthedocs.io/installation.html)
* [Selenium Webdriver with Python 3 Udemy Course](https://www.udemy.com/course/selenium-webdriver-with-python3/)
* [The Selenium Guidebook](https://seleniumguidebook.com/)
