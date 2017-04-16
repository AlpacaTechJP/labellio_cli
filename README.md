Labellio Command Line Interface
===

[![Join the chat at https://gitter.im/AlpacaDB/labellio_cli](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/AlpacaDB/labellio_cli?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Example
---
    $ ls model
    caffemodel  deploy.prototxt  label.json  labellio.json  mean.binaryproto
    $ ls image
    hippopotamus1.jpg  hippopotamus2.jpg  lemon1.jpg  lemon2.jpg
    $ python ~/labellio/bin/labellio_classify model/ image/ 2> /dev/null
    image/hippopotamus1.jpg hippopotamus    [  9.99993682e-01   6.26982774e-06]
    image/hippopotamus2.jpg hippopotamus    [  1.00000000e+00   2.43120479e-09]
    image/lemon1.jpg        lemon   [  6.11703884e-13   1.00000000e+00]
    image/lemon2.jpg        lemon   [  7.23245248e-12   1.00000000e+00]
