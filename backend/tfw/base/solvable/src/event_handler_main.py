import logging
from os.path import dirname, realpath, join
from functools import partial

from tornado.ioloop import IOLoop

from tfw.fsm import YamlFSM
from tfw.event_handlers import FSMAwareEventHandler
from tfw.components.ide import IdeHandler, DeployHandler
from tfw.components.terminal import TerminalHandler
from tfw.components.frontend import FrontendProxyHandler, FrontendReadyHandler
from tfw.components.frontend import ConsoleLogsHandler, MessageQueueHandler, FrontendConfigHandler
from tfw.components.process_management import ProcessHandler, ProcessLogHandler
from tfw.components.fsm import FSMHandler
from tfw.main import EventHandlerFactory, setup_logger, setup_signal_handlers
from tfw.config import TFWENV, TAOENV

from custom_handlers import CenatorHandler, TestCommandsHandler, messageFSMStepsHandler

LOG = logging.getLogger(__name__)
here = dirname(realpath(__file__))



def main():
    # pylint: disable=unused-variable,too-many-locals
    setup_logger(__file__)

    eh_factory = EventHandlerFactory()
    # TFW builtin EventHandlers (required for their respective functionalities)
    # TFW FSM
    fsm_eh = eh_factory.build(FSMHandler(
        fsm_type=partial(
            YamlFSM,
            'test_fsm.yml',
            {}  # jinja2 variables, empty dict enables jinja2 without any variables
        )
    ))
    # Web IDE backend
    ide_eh = eh_factory.build(IdeHandler(
        patterns=['/home/user/workdir/*']
    ))
    deploy_eh = eh_factory.build(DeployHandler())
    # Web shell backend
    terminal_eh = eh_factory.build(TerminalHandler(
        port=TFWENV.TERMINAL_PORT,
        user=TAOENV.USER,
        working_directory=TFWENV.TERMINADO_WD,
        histfile=TFWENV.HISTFILE
    ))
    # Handles 'deploy' button clicks
    process_eh = eh_factory.build(ProcessHandler(
        supervisor_uri=TFWENV.SUPERVISOR_HTTP_URI
    ))
    # Sends live logs of webservice process to frontend
    processlog_eh = eh_factory.build(ProcessLogHandler(
        process_name='webservice',
        supervisor_uri=TFWENV.SUPERVISOR_HTTP_URI,
        log_tail=2000
    ))
    # Proxies frontend API calls to frontend
    frontendproxy_eh = eh_factory.build(FrontendProxyHandler())
    # Initiates first FSM step
    frontendready = FrontendReadyHandler('step_1')
    frontendready_eh = eh_factory.build(frontendready)
    frontendready.stop = frontendready_eh.stop
    # Configures frontend
    frontendconfig_eh = eh_factory.build(
        FrontendConfigHandler(join(here, 'frontend_config.yaml'))
    )
    # Manages message queues
    messagequeue_eh = eh_factory.build(MessageQueueHandler(25))
    # Writes live logs to console on frontend
    console_logs_eh = eh_factory.build(ConsoleLogsHandler(stream='stdout'))

    # Replace these with your custom event handlers
    # Echoes executed commands to messages
    cenator_eh = eh_factory.build(CenatorHandler())
    # Echoes FSM steps
    message_fsm_steps_eh = eh_factory.build(
        messageFSMStepsHandler,
        event_handler_type=FSMAwareEventHandler
    )
    # Catches special commands
    commands_eh = eh_factory.build(TestCommandsHandler(
        bashrc=f'/home/{TAOENV.USER}/.bashrc'
    ))

    setup_signal_handlers()
    IOLoop.current().start()


if __name__ == '__main__':
    main()
