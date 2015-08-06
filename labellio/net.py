# -*- coding: utf-8 -*-
from __future__ import print_function

import caffe
import subprocess
import cStringIO
import re


def select_device(gpu=False, cpu=False, **kwargs):
    if gpu and cpu:
        raise RuntimeError("Invalid Parameter: gpu=True and cpu=True")

    if gpu:
        caffe.set_mode_gpu()
        return

    if cpu:
        caffe.set_mode_cpu()
        return

    # auto detect
    try:
        stdout = subprocess.check_output("nvidia-smi -q -a".split(" "))
        check_n_gpu = re.compile("^Attached GPUs\s+:\s+(\d+)$")
        n_gpu = 0
        for line in cStringIO.StringIO(stdout):
            m = check_n_gpu.match(line)
            if m is not None:
                assert(n_gpu == 0)
                n_gpu = int(m.group(1))

        if n_gpu > 0:
            caffe.set_mode_gpu()
        else:
            caffe.set_mode_cpu()

    except (subprocess.CalledProcessError, OSError):
        caffe.set_mode_cpu()


class Net(caffe.Net):
    def __init__(self, config, **kwargs):
        super(Net, self).__init__(str(config.deploy_file), str(config.model_file), caffe.TEST)
        select_device(**kwargs)

