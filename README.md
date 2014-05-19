# Docker registry glance driver

This is a [docker-registry backend driver](https://github.com/dotcloud/docker-registry/tree/master/depends/docker-registry-core) based on the [glance](http://reverbrain.com/glance/) key-value storage.

[![PyPI version][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]

## Usage

Assuming you have a working docker-registry and glance setup.

`pip install docker-registry-driver-glance`

Edit your configuration so that `storage` reads `glance`.


## Options

You may add any of the following to your main docker-registry configuration to further configure it.


Example:
```yaml
```

## Developer setup

Clone this.

Get your python ready:

```
sudo apt-get install python-pip
sudo pip install tox
```

You are ready to hack.
In order to verify what you did is ok:
 * run `tox`
 * alternatively, run `python setup.py nosetests` to only run tests on the system python

This will run the tests provided by [`docker-registry-core`](https://github.com/dotcloud/docker-registry/tree/master/depends/docker-registry-core)


## License

This is licensed under the Apache license.
Most of the code here comes from docker-registry, under an Apache license as well.

[pypi-url]: https://pypi.python.org/pypi/docker-registry-driver-glance
[pypi-image]: https://badge.fury.io/py/docker-registry-driver-glance.svg

[travis-url]: http://travis-ci.org/dmp42/docker-registry-driver-glance
[travis-image]: https://secure.travis-ci.org/dmp42/docker-registry-driver-glance.png?branch=master
