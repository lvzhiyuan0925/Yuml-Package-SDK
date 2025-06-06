from typing import Any
from PyQt5.QtWidgets import QWidget
from collections.abc import Hashable

class Globals:
    def globals(self, name: Hashable, value: Any) -> None:  ...
    def getGlobals(self, name: Hashable) -> Any:  ...
    def delGlobals(self, name: Hashable) -> None:  ...

class Default:
    def string(self, value: str) -> Any: ...
    def onClicked(self, scope: str, widget: QWidget, value: Any = None) -> None: ...
    def call_block(self, scope: list | str, accept: Any = None) -> None: ...

class Log:
    @staticmethod
    def debug_print(msg: Any) -> None:  ...
    @staticmethod
    def info_print(msg: Any) -> None: ...
    @staticmethod
    def error_print(msg: Any, _type: str) -> None: ...
