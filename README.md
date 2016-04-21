
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


Then install this req.txt file
```
pip install -r cs-requirements.txt
```

To check this process worked, make sure you're in the directory where the TRAXLZU12903D05F94.h5 test file is.

open python or ipython in the terminal, run

```
from tables import *
h5file = open_file("TRAXLZU12903D05F94.h5", mode = "w", title = "Test file")
``` 

Follow other tutorials in pytables documentation!