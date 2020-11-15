from opcode import HAVE_ARGUMENT as HAVE_ARGUMENT
from typing import Any, Optional

unsafe_eval = eval
__all__: Any
_ALLOWED_MODULES: Any
_UNSAFE_ATTRIBUTES: Any

def to_opcodes(opnames: Any, _opmap: Any = ...) -> None: ...

_BLACKLIST: Any
_CONST_OPCODES: Any
_operations: Any
_EXPR_OPCODES: Any
_SAFE_OPCODES: Any
_logger: Any

def assert_no_dunder_name(code_obj: Any, expr: Any) -> None: ...
def assert_valid_codeobj(allowed_codes: Any, code_obj: Any, expr: Any) -> None: ...
def test_expr(expr: Any, allowed_codes: Any, mode: str = ...): ...
def const_eval(expr: Any): ...
def expr_eval(expr: Any): ...
def _import(name: Any, globals: Optional[Any] = ..., locals: Optional[Any] = ..., fromlist: Optional[Any] = ..., level: int = ...): ...

_BUILTINS: Any

def safe_eval(expr: Any, globals_dict: Optional[Any] = ..., locals_dict: Optional[Any] = ..., mode: str = ..., nocopy: bool = ..., locals_builtins: bool = ...): ...
def test_python_expr(expr: Any, mode: str = ...): ...