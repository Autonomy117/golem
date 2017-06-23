import multiprocessing
import subprocess
import sys

"""GNUtee-like tool for Python built using multiprocessing module
Will will terminate when subproc will stop.
"""
class MPTee(object):
    def __init__(self, subproc, filename):
        """subproc  - should be created using Popen(..., stdout=subprocess.PIPE)
        """
        self.filename = filename
        self.subproc = subproc
        self.p = multiprocessing.Process(target=self._run, args=())

    def join(self):
        self.p.join()

    def start(self):
        self.p.start()

    def _run(self):
        with open(self.filename, 'a', 1) as f:
            while True:
                out = self.subproc.stdout.read(1)
                if out == '' and self.subproc.poll() is not None:
                    break
                if out != '':
                    sys.stdout.write(out)
                    sys.stdout.flush()
                    f.write(out)
