from typing import Optional


class Log:
    def __init__(self, param: str, type: Optional[str] = None):
        if type in [None, 'info']:
            print('\n\033[34mℹ', param, '\033[0m')  # Blue color for info
            ...
        elif type == 'warning':
            print('\n\033[33m⚠', param, '\033[0m')  # Yellow color for warning
            ...
        elif type == 'error':
            exit('\n\033[31m❌', param, '\033[0m')  # Red color for error
            ...
        elif type == 'success':
            print('\n\033[32m✓', param, '\033[0m')  # Green color for success
            ...
        else:
            exit("invalid log type: [ {} ]".format(type))
            ...