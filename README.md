# Self-healing Selenium Tests in Robot Framework using Healenium

Healenium is a tool based on Selenium that provides capability to heal (re-generate) a locator once the element could not be found. 
Read more about this tool at https://healenium.io

This is solution is based on the Healenium Docker containers for Python provided by the open-source project at https://github.com/healenium/healenium-example-python

## Disclaimer
Please note that this is just a **proof of concept**, testing and debugging is still ongoing. 

We would be happy to know your comments or issues on following e-mail: lucie.lavickova@tesena.com

## Prerequisities
1. install **Python** v3.9 or newer: https://www.python.org/downloads, including **pip**
2. using commandline terminal, navigate to the project root and **activate the virtual environment**
   * ```.\venv\Scripts\activate```
3. **install required libraries** using pip:
   * ```pip install -r requirements.txt```
7. install and **run Docker Desktop**: https://www.docker.com/products/docker-desktop
8. in the project directory, start commandline terminal and **start the Healenium Docker containers** using following commands:
   * ```docker-compose up -d``` - download Docker images and create containers
   * ```docker ps``` - list the created containers
9. verify that following **containers are up and running** (either in the previous terminal output or directly in Docker Desktop client): 
   * healenium/hlm-backend 
   * postgres:11-alpine
   * healenium/hlm-proxy
   * healenium/hlm-selenium-4-standalone-xpra
   * healenium/hlm-selector-imitator`

## How to execute tests
Using commandline from project root:
   * ```robot -d results tests\healenium_test.robot```

To see the test execution, you can open http://localhost:8086 in your browser (replace localhost by the name of your server if running remotely)
