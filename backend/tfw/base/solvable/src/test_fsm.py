# This defines an FSM equvivalent to test_fsm.yml

from os.path import exists

from tfw.fsm import LinearFSM
from tfw.components.frontend import MessageSender
from tfw.main import TFWUplinkConnector


class TestFSM(LinearFSM):
    # pylint: disable=unused-argument

    def __init__(self):
        super().__init__(6)
        self.uplink = TFWUplinkConnector()
        self.message_sender = MessageSender(self.uplink)
        self.subscribe_predicate('step_3', self.step_3_allowed)

    @staticmethod
    def step_3_allowed():
        return exists('/home/user/workdir/allow_step_3')

    def on_enter_1(self, event_data):
        self.message_sender.send('FSM', 'Entered state 1!')

    def on_enter_2(self, event_data):
        filename = '/home/user/workdir/cat.txt'
        with open(filename, 'w') as ofile:
            ofile.write('As you can see it is possible to write arbitrary python code here.')
        self.message_sender.send('FSM', f'Entered state 2! Written stuff to {filename}')

    def on_enter_3(self, event_data):
        self.message_sender.send('FSM', 'Entered state 3!')

    def on_enter_4(self, event_data):
        self.message_sender.send('FSM', 'Entered state 4!')

    def on_enter_5(self, event_data):
        self.message_sender.send('FSM', 'Entered state 5!')
