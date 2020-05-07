import os
import cv2   
from xml.dom import minidom
import numpy as np
from distributed.protocol import h5py
from skimage.measure import label
from tqdm import tqdm

"""
This method is used to generate ground truth values.

"""
def generate_gt(filename,image):

    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    edged = cv2.Canny(gray, 30, 200) 
    cv2.waitKey(0) 
    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    cv2.waitKey(0) 
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    cv2.destroyAllWindows()
    cv2.imwrite(filename, gray) 
    print(np.unique(gray))


def label_pixels(filename,image):
    
     x = np.asarray(image)
     x[x == 150 ] = 1  #green
     x[x == 255 ] = 2  #blue
     print(np.unique(x))
     image2 =  x.astype(np.uint8)
     cv2.imwrite(filename, image2)




"""
    Preprocesses external data and puts them in training directory.
    Modified the codes provided in 
    https://www.kaggle.com/voglinio/external-h-e-data-with-mask-annotations
    
    Made changes regarding mask generation ,image generation.
"""

def preprocess_external_data(annot_path, images_path,gt_path):

    if os.path.exists(annot_path) and os.path.exists(images_path) and os.path.exists(gt_path):
        for annot_num, image_name in tqdm(enumerate(os.listdir(images_path))):
            image_id = image_name.split('.')[0]
            img = cv2.imread(os.path.join(images_path, image_name))
            gt_xml = image_id + '.xml'
            gt_tree = minidom.parse(os.path.join(annot_path, gt_xml))
            gt_regions = gt_tree.getElementsByTagName("Regions")[0].getElementsByTagName("Region")
            mask = np.zeros((img.shape[0], img.shape[1]))
            for mm, region in enumerate(gt_regions):
                vertices = region.getElementsByTagName("Vertex")
                nucleus = []
                for vertex in vertices:
                    x = float(vertex.attributes["X"].value)
                    y = float(vertex.attributes["Y"].value)
                    nucleus.append([x, y])
                nucleus = np.array(nucleus)
                nucleus = nucleus.reshape((-1, 1, 2))
                nucleus = np.round(nucleus)
                nucleus = nucleus.astype(np.int32)
                nucleus.shape
                cv2.fillPoly(mask, [nucleus], mm+1)
            cv2.imwrite(gt_path+image_id + '.png', mask)

    #         for mm, (img_piece, mask_piece) in enumerate(zip(split_image(img), split_image(mask))):
    #
    #             path = gt_path+image_id+'_'+str(mm)
    #             if not os.path.isdir(path):
    #                 os.mkdir(path)
    #             if not os.path.isdir(path+'/images/'):
    #                 os.mkdir(path+'/images/')
    #
    #             if not os.path.isdir(path+'/masks/'):
    #                 os.mkdir(path+'/masks/')
    #             fname = path + '/images/' + image_id+'_'+str(mm) + '.png'
    #             cv2.imwrite(fname, img_piece)
    #
    #             mask_piece = label(mask_piece)
    #
    #             mask_piece = np.repeat(
    #                 mask_piece[:, :, np.newaxis], mask_piece.max(), axis=-1)
    #             mask_piece = np.equal(mask_piece, np.ones_like(
    #                 mask_piece)*np.arange(1, mask_piece.max()+1)).astype(np.uint8)
    #
    #             fname = path+'/masks/'+image_id+'_'+str(mm)+'.h5'
    #             with h5py.File(fname, "w") as hf:
    #                 hf.create_dataset("arr", data=mask_piece)
    #
    # else:
    #     print('One of the paths provided does not exist')




if __name__ == "__main__":
    

      count = 1
      for root, dirs, files in os.walk('D:\\Spring2020\\CV\\Project\\Workspace\\Model23\\SegMed\\datasets\\MonuSeg\\test\\gt\\', topdown=False):
          for name in files:
              image = cv2.imread(name)
              cv2.waitKey(0)
              #filename = str(count)+'_gt.bmp'
              x = np.asarray(image)
              print(np.unique(x))
              #x[x > 0 ] = 255
              #image =  x.astype(np.uint8)
              #generate_gt(name,image)
              #label_pixels(name,image)
              #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
              #cv2.imwrite(name,gray)
              count += 1

#    annotation_path = 'D:\\Spring2020\\CV\\Project\\Workspace\\Model23\\SegMed\\datasets\\MonuSeg\\test\\gt_an\\'
#    images_path = 'D:\\Spring2020\\CV\\Project\\Workspace\\Model23\\SegMed\\datasets\\MonuSeg\\test\\images\\'
#    ground_truth = 'D:\\Spring2020\\CV\\Project\\Workspace\\Model23\\SegMed\\datasets\\MonuSeg\\test\\gt\\'
#    preprocess_external_data(annotation_path,images_path,ground_truth)
             
   
    