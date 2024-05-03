import time

def datetime_to_epoch(datetime_str: str) -> int:
    """
    Convert a formatted datetime string to Epoch time.

    Args:
        datetime_str (str): A formatted datetime string (e.g., 'YYYY-MM-DD HH:MM:SS').

    Returns:
        int: The corresponding Epoch time.
    """
    return int(time.mktime(time.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')))

print(datetime_to_epoch('2024-04-16 00:00:00'))


def timestamper(mode: str="D") -> str:
    year, month, day, *_ = time.localtime()
    local_time = f"{year}-{month}-{day} 00:00:00"
    epoch_time = datetime_to_epoch(local_time)
    return '<t:{}:{}>'.format(epoch_time, mode)

print(timestamper())