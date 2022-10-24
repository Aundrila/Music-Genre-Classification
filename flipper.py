import os

import matplotlib
matplotlib.use('agg')

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.pyplot import imread
from matplotlib.pyplot import imsave
from tqdm import tqdm
import pylab

import librosa
from librosa import display
import numpy as np



IMG_DIR = 'spec_all_1000/'
img = os.listdir(IMG_DIR)

DEST = 'spec_all_1000_flipped/'

for i in tqdm(img):
	imgarr = imread(IMG_DIR+i)
	fed = np.fliplr(imgarr)
	imsave(DEST+i[:-4]+"_flipped.jpg", fed)

