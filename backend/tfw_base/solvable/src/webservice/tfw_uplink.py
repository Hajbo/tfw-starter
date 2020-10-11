from os import mkfifo, remove
from os.path import join
from contextlib import suppress
from json import dumps

from pipe_io import PipeWriter

TFW_PIPES_DIR = '/run/tfw'


class TFWUplink:
    def __init__(self):
        self._send_pipe = join(TFW_PIPES_DIR, 'webservice_send')
        with suppress(FileExistsError):
            mkfifo(self._send_pipe)
        self._pipe_writer = PipeWriter(self._send_pipe)

    def send_message(self, message):
        self._pipe_writer.send_message(dumps(message).encode())

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        self.close()

    def close(self):
        self._pipe_writer.close()
        remove(self._send_pipe)
