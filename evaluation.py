import cv2
import numpy as np
from scipy.ndimage.morphology import binary_fill_holes
import utils
from skimage.measure import find_contours
import os
# def load_mask(path,image_id):
#     """Generate instance masks for images of the given image ID.
#     """

#     mask_ = cv2.imread(path  + image_id, 0)
#     mask_ = np.where(mask_ > 128, 1, 0)
#     # Fill holes in the mask
#     mask = []
#     mask_ = binary_fill_holes(mask_).astype(np.int32)
#     # Add mask only if its area is larger than one pixel
#     if np.sum(mask_) >= 1:
#         mask.append(np.squeeze(mask_))

#     mask = np.stack(mask, axis=-1)
#     mask = mask.astype(np.uint8)

#     # Class ids: all ones since all are foreground objects
#     class_ids = np.ones(mask.shape[2])

#     return mask.astype(np.uint8), class_ids.astype(np.int8)

def load_mask(path,image_id):
    """Generate instance masks for images of the given image ID.
    """

    mask_ = cv2.imread(path  + image_id, 0)
    mask_ = np.where(mask_ > 128, 1, 0)
    # Fill holes in the mask
    mask = []
    mask_ = binary_fill_holes(mask_).astype(np.int32)
    # Add mask only if its area is larger than one pixel
    if np.sum(mask_) >= 1:
        mask.append(np.squeeze(mask_))

    mask = np.stack(mask, axis=-1)
    mask = mask.astype(np.uint8)

    # Class ids: all ones since all are foreground objects
    class_ids = np.ones(mask.shape[2])

    return mask.astype(np.uint8)

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from predict import create_masks
path = 'iou/'
# pred_id ='Pred/02_1.png'
# gt_id ='Gt/02_1.png'
# pred_masks = load_mask(path,pred_id)
# true_masks = load_mask(path,gt_id )


val_path = 'iou/Pred'
val_list = os.listdir(val_path)
print(val_list)

create_masks(path,val_list, save_plots=False)



# for i in val_list:
#     print(i)
# contours_tm = find_contours(true_masks[..., 0], 0.5, fully_connected='high')
# contours_pm = find_contours(pred_masks[..., 0], 0.5, fully_connected='high')
# fig = plt.figure()
# gs = gridspec.GridSpec(1, 1)
# ax = fig.add_subplot(gs[0])

# for n, contour in enumerate(contours_tm):

#     ax.plot(contour[:, 1], contour[:, 0], linewidth=1, color='r')
    
    
