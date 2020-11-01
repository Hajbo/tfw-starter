import logging
from json import loads, JSONDecodeError

from tfw.components.frontend import MessageSender
from tfw.components.terminal import TerminalCommandsHandler
from tfw.main import TFWUplinkConnector

LOG = logging.getLogger(__name__)


class CenatorHandler:
    keys = ['history.bash']

    def handle_event(self, message, connector):  # pylint: disable=no-self-use
        command = message['command']
        LOG.debug('User executed command: "%s"', command)
        MessageSender(connector).send(f'You\'ve executed "{command}"', originator='JOHN CENA')


class TestCommandsHandler(TerminalCommandsHandler):
    # pylint: disable=unused-argument,attribute-defined-outside-init,no-self-use
    def command_sendmessage(self, *args):
        if not args:
            message_template = """'{"key": ""}'"""
            TFWUplinkConnector().send_message({
                'key': 'terminal.write',
                'command': f'sendmessage {message_template}'
            })
        else:
            try:
                TFWUplinkConnector().send_message(loads(args[0]))
            except JSONDecodeError:
                LOG.error('IGNORING MESSAGE: Invalid message received: %s', args[0])


def messageFSMStepsHandler(message, connector):
    """
    When the FSM steps this method is invoked.
    Receives a 'data' field from an fsm_update message as kwargs.
    """
    MessageSender(connector).send(
        f'FSM has stepped from state "{message["last_event"]["from_state"]}" '
        f'to state "{message["current_state"]}" in response to trigger "{message["last_event"]["trigger"]}"',
        originator='FSM info'
    )
