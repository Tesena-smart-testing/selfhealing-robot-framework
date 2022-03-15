# Set up Selfhealing Robot Framework with Podman in Ubuntu OS (Linux)
Podman is used as an alternative to Docker, which could be a security issue in some companies. Podman offers a safer option to mitigate the security risks. However, Podman can be used in Linux OS only, there is no support for Windows OS at this moment. 

This guide offers a solution for Ubuntu OS.

## Python
- install python: ```sudo apt install python3```
- install pip: ```sudo apt install python3-pip```
- install python virtual environment: ```sudo apt install python3.8-venv```
## Podman
- install Podman: https://www.cyberithub.com/how-to-install-podman-on-ubuntu-20-04-lts-step-by-step/
- if there is a problem with public key signature, follow https://linuxconfig.org/ubuntu-20-04-gpg-error-the-following-signatures-couldn-t-be-verified
- install podman-compose: ```sudo pip3 install podman-compose```
## Selenium Browser Driver
- download browser driver for the browser you want to use. For Google Chrome, download https://chromedriver.chromium.org/downloads make sure to select the right version (depending on the version of your browser) for Linux.
- extract the browser driver file to Downloads folder
- add browser driver to your path. The easiest way is to move the file to usr/local/bin, which is already in Path: ```sudo mv ~/Downloads/chromedriver /usr/local/bin```
- verify if moved properly: close the terminal, open it again and execute ```chromedriver --version```. It should show your installed version.
## Git
- install git: ```sudo apt install git```
- in Terminal, navigate to the folder where you want to place the project directory and execute ```git clone https://github.com/Tesena-smart-testing/selfhealing-robot-framework.git```
## Install Robot Framework Libraries
- in Terminal, navigate to the selfhealing robot framework project directory
- create the virtual environment: ```python3 -m venv ./venv```
- activate the virtual environment: ```source venv/bin/activate```
- install libraries: ```pip install -r requirements.txt```
## Start Docker containers using Podman
- navigate to infra folder: ```cd infra```
- start the containers: ```podman-compose up -d```
- when prompted, select the images from docker.io server
## Execute tests:
```robot tests\test.robot```