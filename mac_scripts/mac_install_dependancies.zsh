echo "
〚 install homebrew through provided urlscript from site 〛
"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo "
〚 add homebrew enviroment variables to zsh profile file .zprofile   〛
"
echo >> /Users/$USER/.zprofile
    echo 'eval "$(/usr/local/bin/brew shellenv)"' >> /Users/$USER/.zprofile
    eval "$(/usr/local/bin/brew shellenv)"

echo "
〚 installs python and git  〛
"
brew install python3 git
echo "
〚 installs docker 〛
"
brew install --cask docker




