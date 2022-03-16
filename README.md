# run_poppunk
Run poppunk in python

## 1. Download input data and code
```
git clone git@github.com:muppi1993/run_poppunk.git
```
## 2. Download and unpack database
```
cd run_poppunk
wget https://sketchdb.blob.core.windows.net/public-dbs/GPS_v4_full.tar.bz2
tar -xf GPS_v4_full.tar.bz2
```
If you already have the database saved on your machine, you can also adjust `db_path` in `try_poppunk.py` at line 24 to the location of the database on your machine.
## 3. Install PopPUNK
```
conda install poppunk
```
If you can't use conda yet, you can get [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to use it.
If you can't find the package, you might need to run this first: 
```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

## 4. Run popppunk
```
python3 try_poppunk.py
```
