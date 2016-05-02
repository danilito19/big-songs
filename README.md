
Analysis of million songs dataset
========================

### What is this?
-------------

CS 123 project:

Working with h5 files
-----------

The Million Songs Dataset is made up if many h5 files. We can use pytables to work with h5.

First, make sure you have brew installed. If not, install it. If yes, run

```
brew upgrade 
```

```
brew update
```

Then run,

```
brew install homebrew/science/hdf5
```

To install [pytables](http://www.pytables.org/) (to open h5 files), first create a virtual env. Activate your virtual env

```
source myenv/bin/activate
```

Please remember to include the name of your virtualenv inside .gitignore by doing

```
vim .gitignore
```

And time myvenv/ (or whatever name). This will not include it in our git repo.

Then install this req.txt file
```
pip install -r cs-requirements.txt
```

If this crashes at some point with error about setup.py egg ... don't know how to fix this yet. Try pip install tables, which should work for now.

To check this process worked, make sure you're in the directory where the TRAXLZU12903D05F94.h5 test file is.

To work with h5 files, we will be using a Python wrapper made by those who worked on the data at Columbia. Here is the [documentation](http://labrosa.ee.columbia.edu/millionsong/pages/code). This in our directory is file called hdf5.py. 

Open python or ipython in the terminal, make sure you're in the same directory with the data and the hdf5.py file

```
import hdf5
h5 = hdf5_getters.open_h5_file_read("TRBGBDH12903CE9EA8.h5
hdf5.get_artist_hotttnesss(h5)
``` 

The hdf5.py file has most of the functions we will need to get the attributes for the data.