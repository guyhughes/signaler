from __future__ import unicode_literals

import os
import signal
import unittest

from signaler import Signaler


class TestSignalerDefaultConstructor(unittest.TestCase):

    def setUp(self):
        self.s = Signaler()
        assert self.s, "0 arg constructor failed"

    def test_got_sigint(self):
        os.kill(os.getpid(), signal.SIGINT)
        self.assertTrue(self.s.got_sigint)

    def test_got_sigusr1(self):
        os.kill(os.getpid(), signal.SIGUSR1)
        self.assertTrue(self.s.got_sigusr1)


class TestSignaler(unittest.TestCase):

    def test_constructor_invalid(self):
        with self.assertRaises(ValueError) as context:
            Signaler(0)

        self.assertIn('must be a sequence', str(context.exception))
