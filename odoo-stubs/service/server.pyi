import werkzeug.serving
from typing import Any, Optional

INOTIFY_LISTEN_EVENTS: Any
_logger: Any
SLEEP_INTERVAL: int

def memory_info(process: Any): ...
def set_limit_memory_hard() -> None: ...
def empty_pipe(fd: Any) -> None: ...

class LoggingBaseWSGIServerMixIn:
    def handle_error(self, request: Any, client_address: Any) -> None: ...

class BaseWSGIServerNoBind(LoggingBaseWSGIServerMixIn, werkzeug.serving.BaseWSGIServer):
    def __init__(self, app: Any) -> None: ...
    def server_activate(self) -> None: ...

class RequestHandler(werkzeug.serving.WSGIRequestHandler):
    timeout: int = ...
    def setup(self) -> None: ...

class ThreadedWSGIServerReloadable(LoggingBaseWSGIServerMixIn, werkzeug.serving.ThreadedWSGIServer):
    max_http_threads: Any = ...
    http_threads_sem: Any = ...
    daemon_threads: bool = ...
    def __init__(self, host: Any, port: Any, app: Any) -> None: ...
    reload_socket: bool = ...
    socket: Any = ...
    def server_bind(self) -> None: ...
    def server_activate(self) -> None: ...
    def process_request(self, request: Any, client_address: Any) -> None: ...
    def _handle_request_noblock(self) -> None: ...
    def shutdown_request(self, request: Any) -> None: ...

class FSWatcherBase:
    def handle_file(self, path: Any): ...

class FSWatcherWatchdog(FSWatcherBase):
    observer: Any = ...
    def __init__(self) -> None: ...
    def dispatch(self, event: Any) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class FSWatcherInotify(FSWatcherBase):
    started: bool = ...
    watcher: Any = ...
    def __init__(self) -> None: ...
    def run(self) -> None: ...
    thread: Any = ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class CommonServer:
    app: Any = ...
    interface: Any = ...
    port: Any = ...
    pid: Any = ...
    def __init__(self, app: Any) -> None: ...
    def close_socket(self, sock: Any) -> None: ...

class ThreadedServer(CommonServer):
    main_thread_id: Any = ...
    quit_signals_received: int = ...
    httpd: Any = ...
    limits_reached_threads: Any = ...
    limit_reached_time: Any = ...
    def __init__(self, app: Any) -> None: ...
    def signal_handler(self, sig: Any, frame: Any) -> None: ...
    def process_limit(self) -> None: ...
    def cron_thread(self, number: Any) -> None: ...
    def cron_spawn(self) -> None: ...
    def http_thread(self): ...
    def http_spawn(self) -> None: ...
    def start(self, stop: bool = ...): ...
    def stop(self) -> None: ...
    def run(self, preload: Optional[Any] = ..., stop: bool = ...): ...
    def reload(self) -> None: ...

class GeventServer(CommonServer):
    port: Any = ...
    httpd: Any = ...
    def __init__(self, app: Any) -> None: ...
    def process_limits(self) -> None: ...
    ppid: Any = ...
    def watchdog(self, beat: int = ...) -> None: ...
    client_address: Any = ...
    def start(self): ...
    def stop(self) -> None: ...
    def run(self, preload: Any, stop: Any) -> None: ...

class PreforkServer(CommonServer):
    address: Any = ...
    population: Any = ...
    timeout: Any = ...
    limit_request: Any = ...
    cron_timeout: Any = ...
    beat: int = ...
    app: Any = ...
    pid: Any = ...
    socket: Any = ...
    workers_http: Any = ...
    workers_cron: Any = ...
    workers: Any = ...
    generation: int = ...
    queue: Any = ...
    long_polling_pid: Any = ...
    def __init__(self, app: Any) -> None: ...
    def pipe_new(self): ...
    def pipe_ping(self, pipe: Any) -> None: ...
    def signal_handler(self, sig: Any, frame: Any) -> None: ...
    def worker_spawn(self, klass: Any, workers_registry: Any): ...
    def long_polling_spawn(self) -> None: ...
    def worker_pop(self, pid: Any) -> None: ...
    def worker_kill(self, pid: Any, sig: Any) -> None: ...
    def process_signals(self) -> None: ...
    def process_zombie(self) -> None: ...
    def process_timeout(self) -> None: ...
    def process_spawn(self) -> None: ...
    def sleep(self) -> None: ...
    pipe: Any = ...
    def start(self) -> None: ...
    def stop(self, graceful: bool = ...) -> None: ...
    def run(self, preload: Any, stop: Any): ...

class Worker:
    multi: Any = ...
    watchdog_time: Any = ...
    watchdog_pipe: Any = ...
    eintr_pipe: Any = ...
    watchdog_timeout: Any = ...
    ppid: Any = ...
    pid: Any = ...
    alive: bool = ...
    request_max: Any = ...
    request_count: int = ...
    def __init__(self, multi: Any) -> None: ...
    def setproctitle(self, title: str = ...) -> None: ...
    def close(self) -> None: ...
    def signal_handler(self, sig: Any, frame: Any) -> None: ...
    def signal_time_expired_handler(self, n: Any, stack: Any) -> None: ...
    def sleep(self) -> None: ...
    def check_limits(self) -> None: ...
    def process_work(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...
    def _runloop(self) -> None: ...

class WorkerHTTP(Worker):
    def process_request(self, client: Any, addr: Any) -> None: ...
    def process_work(self) -> None: ...
    server: Any = ...
    def start(self) -> None: ...

class WorkerCron(Worker):
    db_index: int = ...
    watchdog_timeout: Any = ...
    def __init__(self, multi: Any) -> None: ...
    def sleep(self) -> None: ...
    def _db_list(self): ...
    def process_work(self) -> None: ...
    def start(self) -> None: ...

server: Any

def load_server_wide_modules() -> None: ...
def _reexec(updated_modules: Optional[Any] = ...) -> None: ...
def load_test_file_py(registry: Any, test_file: Any) -> None: ...
def preload_registries(dbnames: Any): ...
def start(preload: Optional[Any] = ..., stop: bool = ...): ...
def restart() -> None: ...
