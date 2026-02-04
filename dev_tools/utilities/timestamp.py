def generate_timestamp():
    from time import strftime, localtime
    now = localtime()
    timestamp = strftime("%d_%m_%Y_%H_%M_%S", now)
    return timestamp
