from functools import wraps
from threading import Lock


def thread_safe_singleton(func):
    """
    A decorator that makes a function a thread-safe singleton.
    The decorated function will only be executed once, and its result
    will be cached and returned for all subsequent calls.

    :param func: The function to be decorated.
    :type func: function
    :return: The singleton instance of the function.
    :rtype: function
    """

    lock = Lock()
    instance = None

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function to ensure thread-safe singleton behavior.

        :return: The singleton instance of the function.
        :rtype: function
        """

        nonlocal instance
        if instance is None:
            with lock:
                if instance is None:
                    instance = func(*args, **kwargs)
        return instance

    return wrapper


class Singleton(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Ensure that only one instance of the class is created.

        :return: The singleton instance of the class.
        :rtype: object
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
