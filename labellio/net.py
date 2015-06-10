# -*- coding: utf-8 -*-
from __future__ import print_function

import caffe


class Net(caffe.Net):
    def __init__(self, config, gpu=False):
        super(Net, self).__init__(str(config.deploy_file), str(config.model_file), caffe.TEST)

        if gpu:
            caffe.set_mode_gpu()
        else:
            caffe.set_mode_cpu()

