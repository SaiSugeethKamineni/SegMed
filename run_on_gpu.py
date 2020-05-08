"""
Program to run a specific python code on GUP

author: Akhil 
Added functions "get_contours" and "create masks" to create individual mask layers for Ground truth images in grayscale.
"""

import os
run_GPU = 'set THEANO_FLAGS="mode=FAST_RUN,device=gpu:1,floatX=float32" '
os.system(run_GPU + '& python -u ./train.py ' )
