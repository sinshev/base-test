**DESCRIPTION**

This set of modules is a Python 3.x based framework for Web testing of BaseCRM.

**INSTALLATION**

To be able to run tests you have to install Python 3.x and the following external 
libraries:

0. Python 3.x 
1. Execute the following command to install all requirements from the framework root directory:

    >> pip3 install -U -r python_requirements.txt


**RUNNING**

To run all tests execute the command:
	
	>> python3 -m pytest -s --junitxml=./reports/report.xml ./tests/
	
To run the particular test execute the command:

	>> python3 -m pytest -s --junitxml=./reports/report.xml ./tests/<test_name>

To specify environment for test run execute the command:

	>> python3 -m pytest -s --env=<ENVIRONMENT> tests/

Available environments: `local`, `jenkins`.
	
**OVERVIEW**

The project structure is following:


    ├── base
    │
    ├── pages
    │
    ├── tests
    │
    └── utils


1. `base` - Includes config, resources and base modules.
2. `pages` - Includes PageObject of BaseCRM platform.
3. `tests` - Includes tests for BaseCRM project.
4. `utils` - Includes API helpers and chromedriver.

**JENKINS**

To make possible to run tests on Jenkins, install Xvfb (X virtual framebuffer).
On Ubuntu execute the command:

	>> sudo apt-get install xvfb
