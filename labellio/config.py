# -*- coding: utf-8 -*-
from __future__ import print_function

import caffe.proto.caffe_pb2
import json
import os
import google.protobuf


def get_input_shape(deploy_prototxt):
    # returns shape in (n_data, ch, h, w)
    with open(deploy_prototxt, "rt") as f:
        pb = caffe.proto.caffe_pb2.NetParameter()
        google.protobuf.text_format.Merge(f.read(), pb)
        return pb.input_dim


def check_file(path):
    if not os.path.exists(path):
        raise IOError("File {0} not found.".format(path))


class Config(object):
    def __init__(self, model_dir):
        ini_path = os.path.join(model_dir, "labellio.json")
        check_file(ini_path)

        with open(ini_path) as fp:
            conf = json.loads(fp.read())

        self.model_file = os.path.join(model_dir, conf["model"])
        self.mean_file = os.path.join(model_dir, conf["mean"])
        self.deploy_file = os.path.join(model_dir, conf["deploy"])
        self.label_file = os.path.join(model_dir, conf["label"])

        check_file(self.model_file)
        check_file(self.mean_file)
        check_file(self.deploy_file)
        check_file(self.label_file)

        self.input_shape = get_input_shape(self.deploy_file)
        self.gray = self.input_shape[1] == 1