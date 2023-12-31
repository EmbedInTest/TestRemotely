# Copyright (c) 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
from pathlib import Path

import click


class PIORemotlyCLI(click.MultiCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._root_path = Path(__file__).parent

    def _find_pio_commands(self):
        def _to_module_path(p):
            return (
                "PIORemotly." +
                ".".join(p.relative_to(self._root_path).parts)[:-3]
            )

        result = {}
        for p in self._root_path.rglob("cli.py"):
            # skip this module
            if p.parent == self._root_path:
                continue
            cmd_name = p.parent.name
            result[cmd_name] = _to_module_path(p)
        return result

    def list_commands(self, ctx):
        return sorted(list(self._find_pio_commands()))

    def get_command(self, ctx, cmd_name):
        commands = self._find_pio_commands()
        module = importlib.import_module(commands[cmd_name])
        return getattr(module, "cli")
