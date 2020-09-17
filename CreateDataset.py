# Generate Dataset for Neural Net Model Training

from Model.DLModel.CNN_Model import Cnn
import requests
import os
import cv2
import sys


DOWNLOAD_PATH = r'C:/Users/mahesh/TouristsLens/Model/Dataset'

''' 

Download Images using CSV FILES from URLs Folder 
Use request method to download and save all images in their respective folder    
'''


def saveDownloads(links: list,category: str): 
    # make a new dir with name "category"
    download_count = 1 
    NEW_DOWNLOAD_PATH = os.path.sep.join([DOWNLOAD_PATH, category])

    # print(NEW_DOWNLOAD_PATH)

    if not os.path.exists(NEW_DOWNLOAD_PATH):
        os.mkdir(NEW_DOWNLOAD_PATH) 
    
    for link in links : 
        try : 
            req = requests.get(link,timeout=60)
            file_path = os.path.sep.join([NEW_DOWNLOAD_PATH, '{}.jpg'.format(str(download_count).zfill(6))])
            # Save downloaded Image
            with open(file_path, 'wb' ) as file :
                file.write(req.content)
            print('Downloaded {}'.format(file_path))
            download_count += 1
        except :
            print('Download Failed {}'.format(file_path))

def googleImagesDownload(url_dir_path: str, category_path: str):
    
    # read category file
    CATEGORIES = Cnn.categoryList(category_path)
    
    # CATEGORIES = CATEGORIES[:2]
    # print(CATEGORIES)

    for category in CATEGORIES :
        with open(os.path.sep.join([url_dir_path, category]), 'r') as urls :
            # List of downloadable mounument image links 
            links = urls.read().strip().split('\n') 
            # print(links)

            '''

             Iterate over list and Request for download each link and save it in particular 
             Category folder (create this folder)
             '''
            saveDownloads(links,category)

            
def main() : 
    if(len(sys.argv) != 3) : 
        sys.exit(''' python filename url_dir_path category_file_path \n 
                    Incorrect input to file!, Enter Directory path of URLs ''')
    url_dir_path = sys.argv[1]
    category_path = sys.argv[2]
    googleImagesDownload(url_dir_path, category_path)

if __name__ == '__main__' :
    main()


# DEFAULT URL DIR PATH C:\Users\mahesh\TouristsLens\Model\Dataset\urls
# DEFAULT CATEGORY PATH  = C:\Users\mahesh\TouristsLens\Model\Categories.txt