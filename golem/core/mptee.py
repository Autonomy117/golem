import multiprocessing
import subprocess
import sys

"""GNUtee-like tool for Python built using multiprocessing module
Will will terminate when subproc will stop.
"""
class MPTee(object):
    def __init__(self, subproc, filename, capture_stderr=False):
        """subproc  - should be created using Popen(..., stdout=subprocess.PIPE)
           capture_stderr - if set to True, capture strerr instead
        """
        self.capture_stderr = capture_stderr
        self.filename = filename
        self.subproc = subproc
        self.p = multiprocessing.Process(target=self._run, args=())

    def join(self):
        self.p.join()

    def start(self):
        self.p.start()

    def _run(self):
        if self.capture_stderr:
            input = self.subproc.stderr
            output = sys.stderr
        else
            input = self.subproc.stdout
            output = sys.stdout
        with open(self.filename, 'a', 1) as f:
            while True:
                line = input.read(1)
                if line == '' and self.subproc.poll() is not None:
                    break
                if line != '':
                    output.write(line)
                    output.flush()
                    f.write(line)
