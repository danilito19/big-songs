sudo yum install git
git clone https://github.com/danilito19/big-songs ./songs
cd songs/
sudo pip install -r emr-requirements.txt
# now to install hdf5 and  tables
cd ..
wget ftp://ftp.hdfgroup.org/HDF5/current/src/hdf5-1.8.17.tar.gz
tar -xvzf hdf5-1.8.17.tar.gz
cd hdf5-1.8.17
./configure --prefix=/usr/local/hdf5
make
sudo make check
sudo make install
sudo make check-install
export HDF5_DIR=/usr/local/hdf5
export LD_LIBRARY_PATH=/usr/local/hdf5/lib
cd
sudo pip install cython
git clone https://github.com/PyTables/PyTables.git ./tables
cd tables/
sudo python setup.py build_ext --inplace --hdf5=/usr/local/hdf5/
sudo python setup.py install  --hdf5=/usr/local/hdf5
cd
cd songs/
sudo pip install -r emr-requirements.txt

