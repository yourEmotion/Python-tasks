from traceback import format_exception_only as feo
from contextlib import contextmanager


@contextmanager
def retyper(Old_Exception: type, New_Exception: type) -> None:
    try:
        yield
    except Old_Exception as old:

        def replace_exception(old_exc: Old_Exception) -> New_Exception:
            new_exc = New_Exception()
            new_exc.args = old_exc.args
            return new_exc

        new = replace_exception(old)
        raise new


@contextmanager
def supresser(*Exceptions: type):
    try:
        yield
    except Exceptions:
        pass


@contextmanager
def dumper(stream):
    try:
        yield
    except Exception as exc:
        stream.write(''.join(feo(type(exc), exc)))
        raise exc