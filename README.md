# Unsupervised Nuclei Segmentation method

- We have included two different IPython notebooks
  1. Nuclei Segmentation using Histomics with visualization.ipynb: This notebook has detailed step-by-step processing of image to achieve of goal of segemnetation along with visualizations for one sample image. This gives a clear overview of the process along with data
  2. nuclei_segmentation_unsupervised.ipynb: This notebook has code to run for all the data. To run for each dataset we need to uncomment 
few lines of code in "Main Run" block.

- One of the major caveat with this model is that it just runs on Linux or mac OS (although just tested on Linux machine) but not on Windows due to some datatype issues in communication with cython and python used in HistomicsTK package

- HistomicsTK is the major package which is used to develop this model.
  - Steps to install this package are as below on command prompt:
    1. pip install large-image
    2. pip install cmake
    3. git clone https://github.com/DigitalSlideArchive/HistomicsTK/
    4. cd HistomicsTK/
    5. python -m pip install setuptools-scm Cython>=0.25.2 scikit-build>=0.8.1 cmake>=0.6.0 numpy>=1.12.1
    6. Comment out large-image[sources] in setup.py
    7. python -m pip install -e .
    8. pip install girder-client
    
- With histomicstk is installed and using Linux or mac OS machine can run this model after cloning it
