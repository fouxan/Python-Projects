def add(*args):    # args is a tuple
    ans = 0
    for n in args:
        ans += n

    return ans


def addk(**kw):    # kw is a dictionary and can be accessed with the .get() method or []
    result = 0
    for(key, value) in kw.items():
        result += value

    return result


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(addk(a=1, b=2, c=3, d=4))
