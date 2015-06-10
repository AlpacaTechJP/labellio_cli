# -*- coding: utf-8 -*-
from __future__ import print_function

import caffe


class Mean(object):
    def __init__(self, config):
        # convert binaryproto to numpy array
        blob = caffe.proto.caffe_pb2.BlobProto()
        with open(config.mean_file, "rb") as fp:
            # scale = [0, 255]
            blob.ParseFromString(fp.read())

        self.mean = caffe.io.blobproto_to_array(blob)

        shape = list(self.mean.shape)
        shape.pop(0)

        # K x H x W
        self.mean = self.mean.reshape(shape)
