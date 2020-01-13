#!/usr/bin/env python3

"""Codes came from:
	  - https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/coco.py
"""

import os
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

from absl import app as absl_app
from absl import flags

dataDir = 'cocodataset'
dataType = 'val2017'
valid_annotations_types = ['instances', 'stuff', 'person_keypoints', 'captions']

flags.DEFINE_enum('test', None,
                  ['instances', 'stuff', 'person_keypoints', 'captions'],
                  'Which annotation file do you want to see')

FLAGS = flags.FLAGS


def main(_):

  annotation_paths = [
      '{}/annotations/{}_{}.json'.format(dataDir, anno_type, dataType)
      for anno_type in valid_annotations_types
  ]
  for ann_path in annotation_paths:
    print('{}: {}'.format(ann_path,
                          "True" if os.path.exists(ann_path) else "False"))
    if not os.path.exists(ann_path):
      raise FileExistsError("{} does not exist".format(ann_path))

  # Current COCO API does not support reading panoptic annotation files
  # annFile='{}/annotations/panoptic_{}.json'.format(dataDir, dataType)

  # annotation files for instances/stuffs/person_keypoints/captions
  annFile = '{}/annotations/{}_{}.json'.format(dataDir, FLAGS.test, dataType)

  print('annotation file: ', annFile)

  coco = COCO(annFile)

  cats = coco.loadCats(coco.getCatIds())
  nms = [cat['name'] for cat in cats]
  print('COCO categories: ')
  print(' '.join(nms))

  nms = set([cat['supercategory'] for cat in cats])
  print('COCO supercategories: ')
  print(' '.join(nms))

  # get all images containing given categories, select one at random
  catIds = coco.getCatIds(catNms=['person', 'dog', 'skateboard'])
  print(catIds)
  imgIds = coco.getImgIds(catIds=catIds)
  print(imgIds)
  imgIds = coco.getImgIds(imgIds=[324158])
  print(imgIds)

  image_ids = coco.getImgIds()
  # image_ids.sort()
  # Only display first 5 images
  # image_ids[:5]

  # just select 5 random images
  image_ids = [np.random.choice(image_ids) for _ in range(5)]
  roidb = coco.loadImgs(image_ids)
  for i, entry in enumerate(roidb):
    print('image id: ', image_ids[i])
    print('image file path: ',
          '%s/images/%s/%s' % (dataDir, dataType, entry['file_name']))
    I = io.imread('%s/images/%s/%s' % (dataDir, dataType, entry['file_name']))
    plt.axis('off')
    plt.imshow(I)
    ann_ids = coco.getAnnIds(imgIds=entry['id'], iscrowd=None)
    objs = coco.loadAnns(ann_ids)
    for obj in objs:
      try:
        if isinstance(obj['segmentation'], list):
          obj['segmentation'] = [p for p in obj['segmentation'] if len(p) >= 6]
      except KeyError:
        continue

    coco.showAnns(objs)
    plt.show()


if __name__ == '__main__':
  flags.mark_flag_as_required('test')
  absl_app.run(main)