# Codding Factory Final Project - GeoApp
<div class="row">
  <div class="column">
    <img src="https://github.com/XPONOKPATWP/Codding-Factory-Final-Project/blob/main/images/image_app_readme.png">
</div>

## General Information
<br>
<p>2 default user are provided although registrations and superuser account creation is provided <br> keep in mind that no error messages implementation has been implemented in the corresponding pages</p>
<br>

<ul>
<li><u>Non privileged User</u><br>Username: <b>geo</b><br> Password:<b> rge </b><hr></li>
<li><u> Admin</u><br>Username: <b>giorgos</b><br> Password:<b> Administrator1234@# </b>
</li>
</ul>


## Goal
<br>
<ul>
<li><p>
Calculates the nessecary fuel bettween two regions
it uses nominatum and geopy to find the coordinates of the given location and it defaults to 0,0 if not location is found - Map Page
</p></li>
<li>
<p>
Shows past queries with the ability to delete them -Home Page
</p>
</li>
</ul>

# Automated Install
<br>

## Linux
### Debian Based
##### Without Snaps
 ```
 curl https://raw.githubusercontent.com/XPONOKPATWP/Codding-Factory-Final-Project/refs/heads/main/linux_scripts/deb-apt/deb_distro_init.sh -o deb_distro_init.sh && chmod 755 deb_distro_init.sh && ./deb_distro_init.sh
 ```
<br>

##### With Snaps
 ```
curl https://raw.githubusercontent.com/XPONOKPATWP/Codding-Factory-Final-Project/refs/heads/main/linux_scripts/deb-apt/deb_disto_snap_docker_install.sh -o deb_disto_snap_docker_install.sh && chmod 755 deb_disto_snap_docker_install.sh  && ./deb_disto_snap_docker_install.sh
```
<br>
<br>

## Mac OS - Homebrew
```
curl https://raw.githubusercontent.com/XPONOKPATWP/Codding-Factory-Final-Project/refs/heads/main/mac_scripts/mac_init.zsh -o mac_init.zsh && chmod 755 mac_init.zsh && ./mac_init.zsh
```
<br>
<br>


## Windows - Winget
```
irm https://raw.githubusercontent.com/XPONOKPATWP/Codding-Factory-Final-Project/refs/heads/main/windows_scripts/win_scirpt.ps1 >> win_scirpt.ps1 ; .\win_scirpt.ps1
```
<br>
<hr>

# Manual Instalation

## Install Dependancies
<br>

## Linux
### Debian Based APT Only
##### Update,Upgrade and install python dependancies
 ```
sudo apt update && sudo apt upgrade -y && \
sudo apt install python3 python3-pip python3-venv git -y
 ```
##### Add Docker's official GPG key
 ```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
 ```
##### Add the repository to APT sources: -> /etc/apt/sources.list.d/docker.list

 ```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
 ```
##### Update repositories and install docker

 ```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
 ```
##### Start docker  desktop service
 ```
systemctl --user start docker-desktop
 ```
<br>

### Debian Based with Snap packages
##### Update,Upgrade and install python dependancies and snapd

 ```
sudo apt update && sudo apt upgrade -y \
sudo apt install python3 python3-pip snapd python3-venv git -y \
 ```
##### Install snap package

 ```
sudo snap install docker
 ```
##### Start docker  desktop service

 ```
sudo snap start docker
 ```
<br>

## Mac OS
### Install Homebrew

 ```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
 ```
### Add Homebrew enviroment variables to user's zsh profile

 ```
echo >> /Users/$USER/.zprofile
    echo 'eval "$(/usr/local/bin/brew shellenv)"' >> /Users/$USER/.zprofile
    eval "$(/usr/local/bin/brew shellenv)"
 ```
### Install git, python and docker

 ```
brew install python3 git
brew install --cask docker
 ```
<br>

## Windows
### Install Winget

 ```
Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
 ```
### Install git, python and docker

 ```
winget install -h git.git  Docker.DockerDesktop  Python.Python.3.9  -s winget
 ```
<br>
<hr>

## Project Initialization
### Clone Repositoy
 ```
mkdir georgios_fanourios_karachalios_stagkas
cd georgios_fanourios_karachalios_stagkas
git clone https://github.com/XPONOKPATWP/Codding-Factory-Final-Project.git
cd Codding-Factory-Final-Project/
 ```
<br>
<hr>

### Python Virtual Enviroment
<br>

#### Create and Enter virtual enviroment - Mac OS, Linux
 ```
python3 -m venv .venv
source .venv/bin/activate
 ```
<br>

#### Create and Enter virtual enviroment - Windows
 ```
python -m venv .venv
.venv\Scripts\activate
 ```
<br>
<hr>

### Install Python Modules
<br>

### Mac OS, Linux

 ```
curl https://raw.githubusercontent.com/XPONOKPATWP/Codding-Factory-Final-Project/refs/heads/main/requirements.txt -o requirements.txt
python3 -m pip install -r requirements.txt
 ```
##### Alternative
 ```Alternative
python3 -m pip install asgiref==3.8.1 certifi==2024.12.14 charset-normalizer==3.4.1 Django==5.1.4 django-extensions==3.2.3 geographiclib==2.0 geopy==2.4.1 idna==3.10 packaging==24.2 requests==2.32.3 sqlparse==0.5.3 urllib3==2.3.0
 ```
<br>

### Windows

 ```
irm https://raw.githubusercontent.com/XPONOKPATWP/Codding-Factory-Final-Project/refs/heads/main/requirements.txt >> requirements.txt
pip install -r requirements.txt
 ```
##### Alternative
 ```
pip install asgiref==3.8.1 certifi==2024.12.14 charset-normalizer==3.4.1 Django==5.1.4 django-extensions==3.2.3 geographiclib==2.0 geopy==2.4.1 idna==3.10 packaging==24.2 requests==2.32.3 sqlparse==0.5.3 urllib3==2.3.0
 ```
<br>
<hr>

### CD to project
<br>

#### Mac OS, Linux
 ```
cd geo-app-image-build/src/GeoProject
 ```
<br>

#### Windows

 ```
cd geo-app-image-build\src\GeoProject
 ```
<br>
<hr>

### Create SuperUser
<br>

#### Mac OS, Linux
 ```
python3 manage.py createsuperuser
 ```
#### Windows
 ```
python manage.py createsuperuser
 ```
<br>
<hr>

### Run Server
<br>

#### Mac OS, Linux

 ```
python3 manage.py runserver
 ```
#### Windows
 ```
python manage.py runserver
 ```
<br>
<hr>

# Docker Image
<br>

<p> if you have used the automated script or the manual installation guide you already have
docker-desktop and git installed in your system else refer to the corresponding links
</p>
<ul>
<li>Docker Desktop - https://www.docker.com/products/docker-desktop/</li>
<li>Git - https://git-scm.com/downloads </li>
</ul>

### Clone Repositoy
#### Create a folder and Clone repo inside it
 ```
mkdir georgios_fanourios_karachalios_stagkas
cd georgios_fanourios_karachalios_stagkas
git clone https://github.com/XPONOKPATWP/Codding-Factory-Final-Project.git
cd Codding-Factory-Final-Project/
 ```
### Build Docker Image


 ```
cd geo-app-image-build
docker build -t geo-app-image-codding-factory .
 ```
