from threading import Lock
from typing import Type


class ThreadSafeSingleton(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs) -> Type:
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]
