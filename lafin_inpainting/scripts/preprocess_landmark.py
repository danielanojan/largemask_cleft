import os
from skimage import io
import face_alignment
import argparse
import PIL
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='path to the celeba img_align_celeba folder')
parser.add_argument('--output', type=str, help='path to the output folder')
args = parser.parse_args()

input_path = args.path
output_path = args.output

if not os.path.exists(output_path):
    os.mkdir(output_path)

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType.TWO_D,face_detector='sfd')
filenames = os.listdir(input_path)

for filename in filenames:
    print ('here')
    if filename[-3:] != 'png' and filename[-3:] != 'jpg':
        continue
    print ('here1')
    with open(os.path.join(output_path,filename[:-4]+'_keypoints.txt'), 'w') as f:
        img = np.array(PIL.Image.open(os.path.join(input_path,filename)).convert('RGB'))
        
        print(filename+'\n')
        l_pos = fa.get_landmarks(img)
        for i in range(68):
            f.write(str(l_pos[0][i,0])+' '+str(l_pos[0][i,1])+' ')
        f.write('\n')



