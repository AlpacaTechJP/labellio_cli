from setuptools import setup, find_packages

setup(
    name="labellio",
    version="0.0.1",
    url="", #TODO fill
    description="Labellio command line interface",
    author="AlpacaDB, Inc.",
    license='2-clause BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='deep learning caffe alpacadb alpaca db labellio',
    packages=find_packages(),
    install_requires=['numpy', 'scikit-image', 'protobuf'],
    scripts=['bin/labellio_classify'],
)
