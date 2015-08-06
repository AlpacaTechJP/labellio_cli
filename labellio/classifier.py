# -*- coding: utf-8 -*-
from __future__ import print_function

import numpy as np

from labellio.net import Net


class NetOutput(object):
    def __init__(self, output):
        assert(len(output.shape) == 1)
        self.values = output

    @property
    def best(self):
        return np.argmax(self.values)


class Classifier(object):
    def __init__(self, config, **kwargs):
        self.config = config
        self.net = Net(config, **kwargs)
        self.shape = np.array(self.config.input_shape, dtype=np.uint32)

    def forward_iter(self, data):
        data = np.array(data, dtype=np.float32)
        assert(np.all(data.shape[1:] == self.shape[1:]))
        n_row = self.config.input_shape[0]
        net_input = np.zeros(self.shape, dtype=np.float32)

        s = 0
        e = data.shape[0]

        while s < e:
            n_data = min(e - s, n_row)
            net_input[:n_data, :, :, :] = data[s:s + n_data, :, :, :]
            out = self.net.forward(blobs=[self.net.outputs[0]], **{self.net.inputs[0]: net_input})[self.net.outputs[0]]

            assert(n_row == len(out))
            for i in range(n_data):
                yield(NetOutput(out[i].flatten()))

            s += n_row

            net_input = np.zeros(self.shape, dtype=np.float32)

    def forward(self, data):
        ret = []
        for out in self.forward_iter(data):
            ret.append(out)

        return ret

