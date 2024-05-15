#!/bin/sh

#README:
#This installer is executed this way
#curl -sL "https://raw.githubusercontent.com/n8nhackers/installers/master/installer.sh?user_id=a186f425-305f-496d-bd44-26c7bf15336f" | bash

#we need python to run the script
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Installing python3"
    sudo apt-get install python3
fi

#we need pip to install the required packages
if ! command -v pip3 &> /dev/null
then
    echo "Pip3 is not installed. Installing pip3"
    sudo apt-get install python3-pip
fi

#installing the required packages
pip3 install requests
pip3 install pyfiglet

#running the script
if [ -z "$1" ]
then
    #python3 -c "import requests; exec(requests.get('https://raw.githubusercontent.com/n8nhackers/installers/master/installer.py').text)"
    #run locally
    python3 installer.py
else
    #python3 -c "import requests; exec(requests.get('https://raw.githubusercontent.com/n8nhackers/installers/master/installer.py').text)" --user_id=$1
    #run locally
    python3 installer.py --user_id=$1
fi