# Self-healing Selenium Tests in Robot Framework using Healenium

Healenium is a tool based on Selenium that provides capability to heal (re-generate) a locator once the element could not be found. 
Read more about this tool at https://healenium.io

This is solution is based on the Healenium Docker containers for Python provided by the open-source project at https://github.com/healenium/healenium-example-python

## Disclaimer
Please note that this is just a *proof of concept*, therefore the only supported browser at this moment is **Google Chrome**. Also, the solution has been tested on **Windows OS** only.

## Prerequisities
1. install **Python** v3.7 or newer: https://www.python.org/downloads
4. **download Google Chrome browser driver**. Please check the version of your browser and OS to choose the right driver version: https://chromedriver.chromium.org/downloads
5. **unzip the driver** into some folder (for example C:\WebDrivers or any directory)
6. add the above created **driver path into your System Environment Path**: https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/
2. using commandline, navigate to the project root and **activate the virtual environment**
   * ```venv/Scripts/activate.bat```
3. **install required libraries** using pip:
   * ```pip install -r requirements.txt```
7. install and **run Docker Desktop**: https://www.docker.com/products/docker-desktop
8. in the project directory, start commandline terminal and **start the Healenium Docker containers** using following commands:
   * ```cd infra``` - navigate to infra folder
   * ```docker-compose up -d``` - download Docker images and create containers
   * ```docker ps``` - list the created containers
9. verify that following **containers are up and running** (either in the previous terminal output or directly in Docker Desktop client): 
   * healenium/hlm-backend:3.1.2 
   * postgres:11-alpine
   * healenium/hlm-proxy:1.0
   * healenium/hlm-selenium-4-standalone-xpra:1.0
   * healenium/hlm-selector-imitator:1
10. in the commandline terminal, **return to the project root** from the infra folder:
    * ```cd ..```
11. **open http://localhost:8086** in your browser and wait till the WebSocket Connection is established

## How to execute tests
Using commandline from project root:
   * ```robot tests\test.robot```
