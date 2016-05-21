sudo yum install git
git clone https://github.com/danilito19/big-songs ./songs
cd songs/
sudo pip-2.7 install -r emr-requirements.txt
# now to install hdf5 and  tables
cd ..
wget ftp://ftp.hdfgroup.org/HDF5/current/src/hdf5-1.8.17.tar.gz
tar -xvzf hdf5-1.8.17.tar.gz
cd hdf5-1.8.17
./configure --prefix=/usr/local/hdf5
make
sudo make install
export HDF5_DIR=/usr/local/hdf5
export LD_LIBRARY_PATH=/usr/local/hdf5/lib
cd
sudo pip-2.7 install cython
git clone https://github.com/PyTables/PyTables.git ./tables
cd tables/
sudo python2.7 setup.py build_ext --inplace --hdf5=/usr/local/hdf5/
sudo python2.7 setup.py install --hdf5=/usr/local/hdf5
cd
cd songs/
sudo pip-2.7 install -r emr-requirements.txt
cd ..
# cleanup
sudo rm -rf songs/
sudo rm -rf tables/
sudo rm -rf hdf5-1.8.17/

echo "HDF5_DIR=\"/usr/local/hdf5\"" | sudo tee --append /etc/environment
echo "LD_LIBRARY_PATH=\"/usr/local/hdf5/lib\"" | sudo tee --append /etc/environment