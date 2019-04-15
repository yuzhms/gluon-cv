import os

MXNET_DATA_COCO = os.path.join('/', 'userhome', '.mxnet','datasets', 'coco')

os.environ['MXNET_HOME'] = os.path.join('/', 'userhome', '.mxnet')
os.environ['MXNET_GLUON_REPO'] = 'https://apache-mxnet.s3.cn-north-1.amazonaws.com.cn/'
