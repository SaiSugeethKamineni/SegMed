import numpy as np
import cv2
# import numpy as np
from scipy.ndimage.morphology import binary_fill_holes
import utils

def mean_iou(true_masks, pred_masks):
    """
    Due to https://www.kaggle.com/wcukierski/example-metric-implementation
    """

    y_pred = np.sum((pred_masks.T*np.arange(1, len(pred_masks)+1)).T, axis=0)
    y_true = np.sum((true_masks.T*np.arange(1, len(true_masks)+1)).T, axis=0)
    #
    num_pred = y_pred.max()
    num_true = y_true.max()
    if num_pred < 1:
        num_pred = 1
        y_pred[0, 0] = 1
    # Compute intersection between all objects
    intersection = np.histogram2d(
        y_true.flatten(), y_pred.flatten(), bins=(num_true, num_pred))[0]

    # Compute areas (needed for finding the union between all objects)
    area_true = np.histogram(y_true, bins=num_true)[0]
    area_pred = np.histogram(y_pred, bins=num_pred)[0]
    area_true = np.expand_dims(area_true, -1)
    area_pred = np.expand_dims(area_pred, 0)

    # Compute union
    union = area_true + area_pred - intersection

    # Exclude background from the analysis
    intersection = intersection[1:, 1:]
    union = union[1:, 1:]
    union[union == 0] = 1e-9

    # Compute the intersection over union
    iou = intersection / union

    prec = []

    for t in np.arange(0.5, 1.0, 0.05):
        tp, fp, fn = precision_at(t, iou)
        if (tp + fp + fn) > 0:
            p = tp*1.0 / (tp + fp + fn)
        else:
            p = 0

        prec.append(p)

    return np.mean(prec),iou


# Precision helper function
def precision_at(threshold, iou):
    matches = iou > threshold
    true_positives = np.sum(matches, axis=1) == 1   # Correct objects
    false_positives = np.sum(matches, axis=0) == 0  # Missed objects
    false_negatives = np.sum(matches, axis=1) == 0  # Extra objects
    tp, fp, fn = np.sum(true_positives), np.sum(
        false_positives), np.sum(false_negatives)
    return tp, fp, fn

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
    mask = mask.astype(np.uint8)[:,:,0]
    print(mask.shape)
    # Class ids: all ones since all are foreground objects
    # class_ids = np.ones(mask.shape[2])

    return mask.astype(np.uint8)

import os
val_path = 'iou/Pred'
val_list = os.listdir(val_path)
path = 'iou/'
iou=[]
precision=[]
for l in val_list:
    pred_mask = load_mask(path+'Pred/',l)
    gt_mask = load_mask(path+'Gt/',l)
    # print(pred_mask.shape,gt_mask.shape)
    true_masks=gt_mask; pred_masks=pred_mask;
    Intersection = np.sum(pred_masks*true_masks)
    union = np.sum(true_masks+pred_masks)-np.sum(pred_masks*true_masks)
    iou.append(Intersection/union)
    tp = np.sum((gt_mask==pred_mask) & (gt_mask==1))
    fp = np.sum((pred_mask==1) & (gt_mask==0))
    fn = np.sum((pred_mask==0) & (gt_mask==1))
    precision.append(tp/(tp+fp))
print(np.mean(iou))
print(np.mean(precision))