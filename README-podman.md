# Set up Selfhealing Robot Framework with Podman in Ubuntu OS (Linux)
Podman is used as an alternative to Docker, which could be a security issue in some companies. Podman offers a safer option to mitigate the security risks. However, Podman can be used in Linux OS only, there is no support for Windows OS at this moment. 

This guide offers a solution for **Ubuntu OS.**

## Disclaimer
Please note that this is just a **proof of concept**, testing and debugging is still ongoing. 

We would be happy to know your comments or issues on following e-mail: lucie.lavickova@tesena.com

## Python
- install python: ```sudo apt install python3```
- install pip: ```sudo apt install python3-pip```
- install python virtual environment: ```sudo apt install python3.8-venv```
## Podman
- install Podman: https://www.cyberithub.com/how-to-install-podman-on-ubuntu-20-04-lts-step-by-step/
- if there is a problem with public key signature, follow https://linuxconfig.org/ubuntu-20-04-gpg-error-the-following-signatures-couldn-t-be-verified
- install podman-compose: ```sudo pip3 install podman-compose```
## Git
- install git: ```sudo apt install git```
- in commandline terminal, navigate to the folder where you want to place the project directory and execute ```git clone https://github.com/Tesena-smart-testing/selfhealing-robot-framework.git```
## Install Robot Framework Libraries
- in commandline terminal, navigate to the project directory
- create a new virtual environment: ```python -m venv venv```
- activate the virtual environment: ```source venv/bin/activate```
- install libraries: ```pip install -r requirements.txt```
## Start Docker containers using Podman
- start the containers: ```podman-compose up -d```
- if prompted, select the images from docker.io server
## Execute tests:
Using commandline terminal from project root: ```robot -d results tests\healenium_test.robot```

To see the test execution, you can open http://localhost:8086 in your browser (replace localhost by the name of your server if running remotely)