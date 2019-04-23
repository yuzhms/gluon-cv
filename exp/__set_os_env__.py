import os

MXNET_DATA_COCO = os.path.abspath(os.path.expanduser('~/.mxnet/datasets/coco'))

os.environ['MXNET_HOME'] = os.path.abspath(os.path.expanduser('~/.mxnet'))
os.environ['MXNET_GLUON_REPO'] = 'https://apache-mxnet.s3.cn-north-1.amazonaws.com.cn/'
os.environ['MXNET_CUDNN_AUTOTUNE_DEFAULT'] = '0'