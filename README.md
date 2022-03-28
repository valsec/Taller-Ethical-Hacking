# Taller-Ethical-Hacking

Simple script Python

1.- Enum_Dirs

python3 -m pip install -r requirements.txt

python3 enum_dirs -u URL -d dirs.txt
python3 enum_dirs -u URL -t 30 -d dirs.txt

2.- Banner Grabbing

python3 -m pip install -r requirements.txt

python3 banner_grabbing.py -h 

Options:
  -i IP
  -r Network
  -h Help
  Example: python3 banner_grabbing.py -i 192.168.1.5
  Example: python3 banner_grabbing.py -r 192.168.1.0

3.- Port Scan

python3 -m pip install -r requirements.txt

python3 scan.py 192.168.1.5
python3 scan.py name_device
