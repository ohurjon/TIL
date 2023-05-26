lst = []


def put(n):
    if 0 <= n <= 100:
        lst.append(n)
    else:
        raise ValueError("Out of Range", n)


if __name__ == "__main__":
    try:
        put(90)
        put(-1)
    except ValueError as err:
        param = err.args
        print(param[0], param[1], 'is not in [0,100]')
