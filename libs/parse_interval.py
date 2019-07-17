def get_sensors_parse_interval(interval):

    msg = interval.split(':')
    if msg is None:
        return None

    count = len(msg)
    value = None

    for idx in range(count):
        temp_msg = msg[idx]

        if temp_msg.endswith('s'):
            temp_value = temp_msg[:-1]
            try:
                temp_value = int(temp_value)
                if (temp_value >= 0):
                    if value is None:
                        value = 0
                    value += temp_value
                else:
                    return None
            except:
                return None

        elif temp_msg.endswith('m'):
            temp_value = temp_msg[:-1]
            try:
                temp_value = int(temp_value)
                temp_value *= 60
                if (temp_value >= 0):
                    if value is None:
                        value = 0
                    value += temp_value
                else:
                    return None
            except:
                return None

        elif temp_msg.endswith('h'):
            temp_value = temp_msg[:-1]
            try:
                temp_value = int(temp_value)
                temp_value *= 3600
                if (temp_value >= 0):
                    if value is None:
                        value = 0
                    value += temp_value
            except:
                return None

    return value
