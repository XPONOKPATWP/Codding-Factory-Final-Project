echo "
〚 creating directory georgios_fanourios_karachalios_stagkas_proj 〛
"
mkdir georgios_fanourios_karachalios_stagkas_proj
echo "
〚 changing directory to georgios_fanourios_karachalios_stagkas_proj 〛
"
cd georgios_fanourios_karachalios_stagkas_proj

echo "
 [ installs winget in system ]
  "
Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
echo "
 [ installs docker, git and python ]
  "
winget install -h git.git  Docker.DockerDesktop  Python.Python.3.9  -s winget

echo "
 [ clone repo ]
  "

git clone https://github.com/XPONOKPATWP/Codding-Factory-Final-Project.git

echo "
 [ changing directory to git folder ]
  "
cd Codding-Factory-Final-Project
echo "
 [ create venv ]
  "
python -m venv .venv
echo "
 [ activate venv ]
  "
.venv/Scripts/activate
echo "
 [ install needed packages from requirements.txt ]
  "
pip install -r requirements.txt
echo "
 [ changing to project directory ]
  "
cd geo-app-image-build\src\GeoProject
echo "
 [ create your superuser it is reminded that superuser giorgos  pre exists ]
  "
python manage.py createsuperuser
echo "
 [ server initiates ]
  "
python manage.py runserver
