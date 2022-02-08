import os
import shutil
import numpy as np

selected_images = np.load('selected_images_2.npy')
os.mkdir('pseudo_labeled_2/')

files = os.listdir('unlabeled2017/')

for f in files:
    id = int(f.split('.')[0][3:])
    if id in selected_images:
        shutil.copy('unlabeled2017/img'+str(id)+'.jpg','pseudo_labeled_2/img'+str(id)+'.jpg')