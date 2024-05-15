import os
import sys
import subprocess
import time
import requests
#parse argv

#installer to install the docker 
class Installer:
    def __init__(self, user_id = None):
        self.user_id = user_id
        self.docker = "docker"        
        
        self.setup()
        
    def setup(self):
        is_installed = self.check_docker()
        if not is_installed:
            self.install_docker()
        
    def check_docker(self):
        print("Checking Docker")
        installed = False
        try:
            os.system(self.docker + " --version")
            installed = True
        except:
            print("Docker not installed")
            #self.install_docker()
        
        return installed
    
    def install_docker(self):
        print("Installing Docker")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install apt-transport-https ca-certificates curl software-properties-common")
        os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
        os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
        os.system("sudo apt-get update")
        os.system("sudo apt-get install docker-ce=" + self.docker_version)
        print("Docker Installed")
   
    def check_caprover(self):
        print("Checking Caprover")
        installed = False
        try:
            os.system("caprover --version")
            installed = True
        except:
            print("Caprover not installed")
            #self.install_caprover()
        
        return installed
            
if __name__ == "__main__":
    params = sys.argv
    if len(params) > 1:
        installer = Installer(params[1])
    else:
        installer = Installer()
