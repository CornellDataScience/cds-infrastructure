python3 -m venv env
cd env
source bin/activate
cd ..
cd ..
cd ..
/cds-infrastructure/env/bin/python3 -m pip install --upgrade pip
pip install pipreqs
apt install sudo
sudo apt install git
sudo apt install gcc
pip install requests
pip install -U setuptools

for d in */ ; do
        cd $d
        pwd
        if [ $(git rev-parse --is-inside-git-dir) ]
        then
                if [ -f "requirements.txt" ]
                then
                        cat requirements.txt | sed -e '/^\s*#.*$/d' -e '/^\s*$/d' | xargs -n 1 python -m pip install
                        pip install torch
                else
                        pipreqs .
                        cat requirements.txt | sed -e '/^\s*#.*$/d' -e '/^\s*$/d' | xargs -n 1 python -m pip install
                fi
        fi
        cd ..
done

echo "Python packages and dependencies installed"
