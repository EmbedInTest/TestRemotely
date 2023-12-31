import time

from PIORemotly.api import API
from PIORemotly.run_execution import RunExecution


class Agent:
    _stop: bool

    def __init__(self) -> None:
        self._stop = False

    def start(self, api: API) -> None:
        while (not self._stop):
            if self._check_for_run(api):
                run = self._get_run(api)
                run.run()
            time.sleep(1)

    def stop(self) -> None:
        self._stop = True

    def _check_for_run(self, api: API) -> bool:
        return api.check_for_run()

    def _get_run(self, api: API) -> RunExecution:
        pass
