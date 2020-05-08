import os
run_GPU = 'set THEANO_FLAGS="mode=FAST_RUN,device=gpu:1,floatX=float32" '
os.system(run_GPU + '& python -u ./train.py ' )
