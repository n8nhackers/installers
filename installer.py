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
        self.operating_system = "unknown" 
        
        self.detect_operating_system()
        self.setup()
        
    def detect_operating_system(self):
        #debian
        if os.path.exists("/etc/debian_version"):
            self.operating_system = "debian"
        #redhat
        elif os.path.exists("/etc/redhat-release"):
            self.operating_system = "redhat"
        #centos
        elif os.path.exists("/etc/centos-release"):
            self.operating_system = "redhat"
        #ubuntu
        elif os.path.exists("/etc/lsb-release"):
            self.operating_system = "debian"
        #macosx
        elif os.path.exists("/System/Library/CoreServices/SystemVersion.plist"):
            self.operating_system = "macosx" 
        else:
            print("OS not supported")
        
        print ("Operating System: " + self.operating_system)
        
    def setup(self):
        is_installed = self.check_docker()
        if not is_installed:
            self.install_docker()
            
        if not self.check_caprover():
            self.install_caprover()
        
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
        print("Installing Docker on debian")
        
        #check current operating system
        if self.operating_system == "debian" or self.operating_system == "ubuntu":
            self.install_docker_debian()
        elif self.operating_system == "redhat" or self.operating_system == "centos":
            self.install_docker_redhat()
        elif self.operating_system == "macosx":
            print("MacOSX not supported")
            return
        else:
            print("OS not supported")
            return
                
    def install_docker_debian(self):
        os.system("sudo apt-get update")
        os.system("sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common")
        os.system("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -")
        os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"')
        os.system("sudo apt-get update")
        os.system("sudo apt-get install docker-ce=" + self.docker_version)
        print("Docker Installed")
    
    def install_docker_redhat(self):
        os.system("sudo yum install -y yum-utils")
        os.system("sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo")
        os.system("sudo yum install docker-ce docker-ce-cli containerd.io")
        print("Docker Installed")
   
    def check_caprover(self):
        caprover_port = 3000
        installed = False
        try:
            response = requests.get("http://localhost:" + str(caprover_port))
            if response.status_code == 200:
                installed = True
        except:
            print("Caprover not installed")
            #self.install_caprover()
        
        return installed
    
    def install_caprover(self):
        print("Installing Caprover")
        #docker run -p 80:80 -p 443:443 -p 3000:3000 -e ACCEPTED_TERMS=true -v /var/run/docker.sock:/var/run/docker.sock -v /captain:/captain caprover/caprover
        os.system("docker run -d -p 80:80 -p 443:443 -p 3000:3000 -e ACCEPTED_TERMS=true -v /var/run/docker.sock:/var/run/docker.sock -v /captain:/captain caprover/caprover")
        
        if self.check_caprover():
            print("Caprover Installed")
            
    def check_npm(self):
        print("Checking npm")
        installed = False
        try:
            os.system("npm --version")
            installed = True
        except:
            print("npm not installed")
            #self.install_npm()
        
        return installed
    
    def install_npm(self):
        print("Installing npm")
        if self.operating_system == "debian" or self.operating_system == "ubuntu":
            os.system("sudo apt-get install npm")
        elif self.operating_system == "redhat" or self.operating_system == "centos":
            os.system("sudo yum install npm")
        print("npm Installed")
            
    def install_caprover_cli(self):
        print("Installing Caprover CLI")
        if not self.check_npm():
            self.install_npm()
        os.system("sudo npm install -g caprover")
        print("Caprover CLI Installed")
            
if __name__ == "__main__":
    params = sys.argv
    if len(params) > 1:
        installer = Installer(params[1])
    else:
        installer = Installer()
