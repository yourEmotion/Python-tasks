from sys import exc_info
from traceback import extract_tb


def force_load(module_name):
    module = open(module_name + ".py", "r")
    code = module.readlines()
    # запускаем код, пока он не отработает без ошибок
    # в случае ошибки удаляем нужную строку из кода программы
    while True:
        try:
            exec("".join(code))
            break
        except SyntaxError as error:
            error_line = error.lineno - 1
            code.pop(error_line)
        except Exception:
            exc = exc_info()
            error_traceback = exc[-1]
            error_line = extract_tb(error_traceback)[-1][1] - 1
            code.pop(error_line)
    ldict = {}
    exec("".join(code), globals(), ldict)
    module.close()
    return ldict


force_load("test")
