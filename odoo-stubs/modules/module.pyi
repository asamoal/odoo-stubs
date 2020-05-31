import unittest
from odoo import SUPERUSER_ID as SUPERUSER_ID, api as api
from odoo.tools.misc import mute_logger as mute_logger
from operator import itemgetter as itemgetter
from typing import Any, Optional

MANIFEST_NAMES: Any
README: Any
_logger: Any

def ad_paths(): ...

loaded: Any

class AddonsHook:
    def find_module(self, name: Any, path: Optional[Any] = ...): ...
    def load_module(self, name: Any): ...

class OdooHook:
    def find_module(self, name: Any, path: Optional[Any] = ...): ...
    def load_module(self, name: Any): ...

def initialize_sys_path() -> None: ...
def get_module_path(module: Any, downloaded: bool = ..., display_warning: bool = ...): ...
def get_module_filetree(module: Any, dir: str = ...): ...
def get_resource_path(module: Any, *args: Any): ...
get_module_resource = get_resource_path

def get_resource_from_path(path: Any): ...
def get_module_icon(module: Any): ...
def module_manifest(path: Any): ...
def get_module_root(path: Any): ...
def load_information_from_description_file(module: Any, mod_path: Optional[Any] = ...): ...
def load_openerp_module(module_name: Any) -> None: ...
def get_modules(): ...
def get_modules_with_version(): ...
def adapt_version(version: Any): ...
def get_test_modules(module: Any): ...
def _get_tests_modules(path: Any, module: Any): ...

class OdooTestResult(unittest.result.TestResult):
    def log(self, level: Any, msg: Any, *args: Any, test: Optional[Any] = ..., exc_info: Optional[Any] = ..., extra: Optional[Any] = ..., stack_info: bool = ..., caller_infos: Optional[Any] = ...) -> None: ...
    def getDescription(self, test: Any): ...
    def startTest(self, test: Any) -> None: ...
    def addError(self, test: Any, err: Any) -> None: ...
    def addFailure(self, test: Any, err: Any) -> None: ...
    def addSubTest(self, test: Any, subtest: Any, err: Any) -> None: ...
    def addSkip(self, test: Any, reason: Any) -> None: ...
    def addUnexpectedSuccess(self, test: Any) -> None: ...
    def logError(self, flavour: Any, test: Any, error: Any) -> None: ...
    def getErrorCallerInfo(self, error: Any, test: Any): ...

class OdooTestRunner:
    def run(self, test: Any): ...

current_test: Any

def run_unit_tests(module_name: Any, position: str = ...): ...
def unwrap_suite(test: Any) -> None: ...
