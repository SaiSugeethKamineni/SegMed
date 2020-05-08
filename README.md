Mask RCNN model for Nuclei segmentation

## Model overview

I modified [Inom Mirzaev's](https://github.com/mirzaevinom/data_science_bowl_2018) implementation of Mask RCNN for nuclei segmentation.




### Model and Training

Can use `run_on_gpu.py` to run any of the following codes on gpu.( need to update the corresponding python file in code)

1. Run `python augment_preprocess.py` to pre-process external data and create mosaics from the dataset. (You can skip this step if you only want to train on provided train set)

2. Run `python train.py` to train the model. 

3.  Run `python predict.py` to evaluate model performance on validation set and predict nuclei boundaries on test set.

### Acknowledgements

[1]: https://github.com/matterport/Mask_RCNN
[2]: https://github.com/mirzaevinom/data_science_bowl_2018