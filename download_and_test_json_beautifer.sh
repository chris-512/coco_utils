#!/bin/sh 

COCODATASET_DIR=`pwd`"/cocodataset"

wget https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64
# beautfies json file
chmod +x jq-linux64
if [ -f "$COCODATASET_DIR/annotations/instances_val2017.json" ];then
	./jq-linux64 . $COCODATASET_DIR/annotations/instances_val2017.json > $COCODATASET_DIR/annotations/instances_val2017.beautified.json
else
	echo "instances_val2017.json does not exist. Please download it first."
fi
