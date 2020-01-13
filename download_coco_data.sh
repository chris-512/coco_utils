#!/bin/sh

COCODATASET_DIR=`pwd`"/cocodataset"

mkdir -p $COCODATASET_DIR/images/train2017
mkdir -p $COCODATASET_DIR/images/val2017
mkdir -p $COCODATASET_DIR/annotations

cd $COCODATASET_DIR/images
gsutil -m rsync gs://images.cocodataset.org/train2017 train2017
gsutil -m rsync gs://images.cocodataset.org/val2017 val2017

cd $COCODATASET_DIR/annotations
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
wget http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip
wget http://images.cocodataset.org/annotations/panoptic_annotations_trainval2017.zip

