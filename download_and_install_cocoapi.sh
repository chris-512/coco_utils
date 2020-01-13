#!/bin/sh

git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
echo 'export PYTHONPATH=$PYTHONPATH:'`pwd` >> ~/.bashrc
# or
# echo 'export PYTHONPATH=$PYTHONPATH:'`pwd` >> ~/.zshrc
