echo "
〚 updates and upgrades from currently installed repos 〛
"
sudo apt update && sudo apt upgrade -y \
sudo apt install python3 python3-pip snapd python3-venv git -y \

echo "
〚 installs snapped docker has access only in home directory 〛
"
sudo snap install docker

#start docker  desktop service since you are running linux i suggest podman as a more integrated alternative
sudo snap start docker

echo "
〚 creating directory georgios_fanourios_karachalios_stagkas_proj 〛
"
mkdir georgios_fanourios_karachalios_stagkas_proj
echo "
〚 changing directory to georgios_fanourios_karachalios_stagkas_proj 〛
"
cd georgios_fanourios_karachalios_stagkas_proj

echo "
〚 clone repo 〛
"
git clone https://github.com/XPONOKPATWP/Codding-Factory-Final-Project.git &&
echo "
〚 changing directory to git folder 〛
"
cd Codding-Factory-Final-Project/

echo "
 〚 create venv 〛
 "
python3 -m venv .venv
echo "
 〚 activate venv 〛
 "
source .venv/bin/activate
echo "
 〚 install needed packages from requirements.txt 〛
  "
python3 -m pip install -r requirements.txt

echo "
 〚 changing to project directory 〛
  "
cd geo-app-image-build/src/GeoProject

echo "
 〚 create your superuser it is reminded that superuser giorgos  pre exists 〛
   "
python3 ./manage.py createsuperuser
echo "
 〚 server initiates 〛
   "
python3 ./manage.py runserver




