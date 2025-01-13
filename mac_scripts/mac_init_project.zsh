
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