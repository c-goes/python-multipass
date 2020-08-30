import subprocess
from unittest import TestCase
import multipass

class Test(TestCase):
    def test_launch(self):
        try:
            delete = multipass.delete('pymultipassunittest')
        except subprocess.CalledProcessError:
            pass
        launch: bytes = multipass.launch("pymultipassunittest")
        self.assertIn(b"Launched: pymultipassunittest", launch)
        exec = multipass.exec('pymultipassunittest', ['cat', '/etc/lsb-release'])
        self.assertIn(b'Ubuntu', exec)
        delete = multipass.delete('pymultipassunittest')

    def test_launch_with_paramters(self):
        try:
            delete = multipass.delete('py2multipassunittest2')
        except subprocess.CalledProcessError:
            pass
        launch: bytes = multipass.launch("py2multipassunittest2", '18.04', cpus=1, mem='300m', disk='4G')
        self.assertIn(b"Launched: py2multipassunittest2", launch)
        exec = multipass.exec('py2multipassunittest2', ['cat', '/etc/lsb-release'])
        self.assertIn(b'18.04', exec)
        delete = multipass.delete('py2multipassunittest2')