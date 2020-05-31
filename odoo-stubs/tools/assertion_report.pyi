from typing import Any

class assertion_report:
    successes: int = ...
    failures: int = ...
    def __init__(self) -> None: ...
    def record_success(self) -> None: ...
    def record_failure(self) -> None: ...
    def record_result(self, result: Any) -> None: ...
    def __str__(self): ...
