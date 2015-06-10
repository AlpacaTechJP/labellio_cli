# -*- coding: utf-8 -*-
from __future__ import print_function

import skimage
import numpy as np

import caffe.io
from labellio import mean


def rgb2bgr(img):
    # RGB -> BGR
    return img[:, :, (2, 1, 0)]


def rgb2gray(img):
    # RGB -> Gray
    return skimage.color.rgb2gray(img)[:, :, np.newaxis]


class Image(object):
    def __init__(self, path):
        # H x W x K
        img = caffe.io.load_image(path, color=True)
        assert(len(img.shape) == 3)
        assert(img.shape[2] == 3)
        self.img = img


class Normalizer(object):
    def __init__(self, config):
        # size: H x W
        self.size = (config.input_shape[2], config.input_shape[3])
        self.gray = config.gray
        self.mean = mean.Mean(config).mean

    def __call__(self, image):
        # H x W x K
        img = image.img
        assert(img.shape[2] == 3)

        img = caffe.io.resize_image(img, self.size)

        if self.gray:
            img = rgb2gray(img)
        else:
            img = rgb2bgr(img)

        # K x H x W
        img = img.transpose(2, 0, 1)

        # [0, 256)
        img = img*255
        return img - self.mean


class ImageLoader(object):
    def __init__(self, config):
        self.config = config
        self.normalizer = Normalizer(config)

    def load(self, path):
        return self.normalizer(Image(path))
