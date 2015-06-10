# -*- coding: utf-8 -*-
from __future__ import print_function

import json


class Label(object):
    def __init__(self, config):
        with open(config.label_file) as fp:
            self.label_dict = json.loads(fp.read())

        assert(isinstance(self.label_dict, dict))

        labels = sorted(self.label_dict.items(), key=lambda x: x[1])
        labels, indexes = zip(*labels)
        min_index = indexes[0]
        max_index = indexes[len(indexes)-1]
        assert(min_index == 0)
        assert(max_index == len(indexes)-1)
        assert(list(indexes) == range(min_index, max_index+1))

        self.inv = labels

    def label(self, index):
        return self.inv[index]

