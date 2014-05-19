# -*- coding: utf-8 -*-

import logging

from docker_registry import testing

logger = logging.getLogger(__name__)


class TestBasic(object):
    def test_import(self):
        import docker_registry.drivers.glance  # noqa

    def test_hasstorage(self):
        import docker_registry.drivers.glance as glance # noqa
        assert glance.Storage

    def test_instanciate(self):
        import docker_registry.drivers.glance as glance # noqa
        glance.Storage('somepath', testing.Config({}))


class TestQuery(testing.Query):
    def __init__(self):
        self.scheme = 'glance'


class TestDriver(testing.Driver):
    def __init__(self):
        self.scheme = 'glance'
        self.path = ''
        self.config = testing.Config({})

    def gen_random_string(self, length=16):
        return "%s//%s" % (self._storage.images,
                           super(TestDriver, self).gen_random_string(length))
