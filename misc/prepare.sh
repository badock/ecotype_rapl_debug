#!/usr/bin/env bash


apt install -y python3 python3-pip linux-cpupower dkms git libpthread-stubs0-dev libmpich-dev
pip3 install -r requirements.txt

pushd /root/

# Installing NASA benchmark
wget https://www.nas.nasa.gov/assets/npb/NPB3.4.1.tar.gz
tar -zxvf NPB3.4.1.tar.gz
pushd NPB3.4.1/NPB3.4-MPI
cp config/make.def.template config/make.def
make ep CLASS=D
popd

# Install CoreFreq
git clone https://github.com/cyring/CoreFreq.git
pushd CoreFreq
make
make install
insmod corefreqk.ko
systemctl daemon-reload
popd

popd

exit 0