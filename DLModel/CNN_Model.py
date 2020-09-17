from imutils import paths
import sys
import cv2
import os


class Cnn:
    @staticmethod
    def preprocessing(dataset_path, category_path) :
        for category in Cnn.categoryList(category_path) :
            for image_path in paths.list_images(r'' + dataset_path + '/{}'.format(category)):
                print('Path: ',image_path)
                delete_image = False
                try:
                    image = cv2.imread(image_path)
                
                    if image is None:
                        delete_image = True
                except:
                    delete_image = True
                
                if delete_image:
                    print('Deleting {}'.format(image_path))
                    os.remove(image_path)  
    @staticmethod
    def categoryList(category_path) :
        '''
        Utility function returning list of categories (labels) 
        
        '''
        try:
            with open(category_path,'r') as labels :
                return labels.read().strip().split('\n') 
        except : 
            sys.exit('Invalid Category File!')

    @staticmethod
    def datasetSize(dataset_path):
        size = 0
        classes = os.listdir(dataset_path)
        for name in classes :
            file_path = os.path.sep.join([dataset_path,name])
            _,_,files = next(os.walk(file_path))
            size += len(files)
        return size


