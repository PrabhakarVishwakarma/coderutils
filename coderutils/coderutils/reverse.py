def reverse(value):
    if isinstance(value, str):
        return value[::-1]

    elif isinstance(value, int):
        sign = -1 if value < 0 else 1
        value = abs(value)

        reversed_num = int(str(value)[::-1])

        return sign * reversed_num

    else:
        raise TypeError(
            "Only strings and integers are supported"
        )
