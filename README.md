# Nuclei Boundary Model
This Nuclei boundary model from [1] is used to apply on various datasets after required modifications. 
1. Datasets folder consists  MonuSeg,PSB,TNBC datasets for training and testing.
2. Experiments folder consists three models : Model1 - PSB Dataset , Model2 - TNBC Dataset , Model3 - MonuSeg Dataset. 


# References
[1] Cui, Yuxin, et al. “A Deep Learning Algorithm for One-Step Contour Aware Nuclei Segmentation of Histopathology Images.” Medical \& Biological Engineering \& Computing, vol. 57, no. 9, 2019, pp. 2027–2043., doi:10.1007/s11517-019-02008-8. https://arxiv.org/pdf/1803.02786.pdf



## Requirements

* python 3.5
* numpy
* keras
* tensorflow-gpu
* scipy
* cv2
* skimage
* pillow
* h6py
* configParser


## Training and Testing
First run:

```python
python prepare_dataset.py 
```
to prepare dataset

* Training
Directly run:
```python
python run_training.py
```
At the begining of the training, a folder name "test1" will be created in "experiment". During the training, models will be saved in it. 
* Testing
```python
python run_training.py
```
It will generate a folder name '1' in 'test1'. The predictions will be shown in it.
You may modify configuration.txt to change the experiement settings.

## Licence
The code is licensed under [MIT](https://github.com/easycui/nuclei_segmentation/blob/master/LICENSE). Copyright (c) 2018.　The dataset is obtained from https://nucleisegmentationbenchmark.weebly.com/dataset.html.
