#!/bin/bash

echo "Environment Setup For OpenRAM"
echo
echo "Following tools will be installed: "
echo "1. NgSpice"
echo "2. Xschem"
echo "3. Magic"
echo "4. OpenRAM"
echo
echo
echo "======================================="
echo "------- INSTALLING DEPENDENCIES -------"
echo "======================================="
echo
sudo apt-get update

sudo apt-get install git --assume-yes
sudo apt-get install build-essential bison flex \
libreadline-dev gawk tcl-dev tk-dev libffi-dev git \
graphviz xdot pkg-config python3 --assume-yes
sudo apt install libglu1-mesa-dev freeglut3-dev --assume-yes


sudo apt-get install ngspice --assume-yes

git clone https://github.com/StefanSchippers/xschem.git
cd xschem
./configure
make
sudo make install
cd ../

sudo apt-get update
sudo apt-get install m4 --assume-yes
sudo apt-get install libx11-dev --assume-yes
sudo apt-get install tcsh --assume-yes
sudo apt-get install tclsh --assume-yes
git clone https://github.com/RTimothyEdwards/magic.git
cd magic
./configure
make
sudo make install
cd ../

sudo apt-get update
sudo apt-get -y install python3-pip --assume-yes
pip3 install numpy
pip3 install scipy

git clone https://github.com/VLSIDA/OpenRAM.git
cd OpenRAM
export OPENRAM_FOLDER_PATH=$(pwd)

echo "================================="
echo "======= Done Installtion ========"
echo
echo
echo "For Better Performance Added Following lines to .bashrc :"
echo "export OPENRAM_HOME=\"$OPENRAM_FOLDER_PATH/compiler"\"
echo "export OPENRAM_TECH=\"$OPENRAM_FOLDER_PATH/technology"\"
echo "export PYTHONPATH=\"$PYTHONPATH:$OPENRAM_HOME"\"
echo
echo "exiting"