echo "
〚 Updates,Upgrades, Installs Curl 〛
"
sudo apt update && sudo apt upgrade -y && sudo apt install curl -y &&
echo "
〚 creating directory georgios_fanourios_karachalios_stagkas_proj 〛
"
mkdir georgios_fanourios_karachalios_stagkas_proj
echo "
〚 changing directory to georgios_fanourios_karachalios_stagkas_proj 〛
"
cd georgios_fanourios_karachalios_stagkas_proj
echo "
〚 downloading dependancies script from repo 〛
"
curl https://raw.githubusercontent.com/XPONOKPATWP/Codding-Factory-Final-Project/refs/heads/main/linux_scripts/deb-apt/deb_install_dependancies.sh -o deb_install_dependancies.sh
echo "
〚 making dependancies script from repo executable 7:rwx , 5:rx, 5:rx 〛
"
chmod 755 deb_install_dependancies.sh
echo "
〚 downloading initialization script from repo 〛
"
curl https://raw.githubusercontent.com/XPONOKPATWP/Codding-Factory-Final-Project/refs/heads/main/linux_scripts/deb-apt/deb_initiate_project.sh -o deb_initiate_project.sh
echo "
〚 making initialization script from repo executable 7:rwx , 5:rx, 5:rx 〛
"
chmod 755 deb_initiate_project.sh
echo "
〚 executing scripts 〛
"
./deb_install_dependancies.sh || true && ./deb_initiate_project.sh
