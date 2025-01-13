sudo apt update && sudo apt upgrade -y && \
sudo apt install python3 python3-pip python3-venv git -y

echo "
 〚 Add Docker through Apt taken from site if you are using ubuntu preferable install it

through snap since it tampers less with the root file-system 〛
 "

echo "
 〚 Add Docker's official GPG key 〛
 "
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo "
 〚 Add the repository to Apt sources: -> /etc/apt/sources.list.d/docker.list 〛
 "
/bin/bash -c "echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"
echo "
〚 Update repository 〛
"
sudo apt-get update

echo "
〚 install docker 〛
"
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

echo "
〚 start docker  desktop service 〛
"
systemctl --user start docker-desktop
