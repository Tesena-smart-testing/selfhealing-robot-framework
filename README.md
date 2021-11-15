# Self-healing Selenium Tests in Robot Framework using Healenium

Healenium is a tool based on Selenium that provides capability to heal (re-generate) a locator once the element could not be found. 
Read more about this tool at https://healenium.io

This solution is based on the Healenium Docker containers for Python provided by the open-source project at https://github.com/healenium/healenium-example-python

## Prerequisities:
1. activate virtual environment using commandline terminal from project root
   * ```venv/Scripts/activate.bat```
2. install required libraries using pip:
   * ```pip install -r requirements.txt```
3. install and run Docker Desktop: https://www.docker.com/products/docker-desktop
4. in the project directory, start commandline terminal and start the Healenium Docker containers using following commands:
   * ```cd infra``` - navigate to infra folder
   * ```docker-compose up -d``` - download Docker images and create containers
   * ```docker ps``` - list the created containers
5. verify that following containers are up and running (either in the previous terminal output or directly in Docker Desktop client): 
   * healenium/hlm-backend:3.1.2 
   * postgres:11-alpine
   * healenium/hlm-proxy:1.0
   * healenium/hlm-selenium-4-standalone-xpra:1.0
   * healenium/hlm-selector-imitator:1
6. in the commandline terminal, return to the project root from the infra folder:
   * ```cd ..```
7. open http://localhost:8086 in your browser and wait till the WebSocket Connection is established


## How to run the tests:
Using commandline from project root:
   * ```robot tests\test.robot```
