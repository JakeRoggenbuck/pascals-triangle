from math import factorial, log, floor, ceil
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from PIL import Image
from IPython.display import display

sns.set_theme()


def pascal(rule=lambda x: x, length: int = 10):
    full = []
    for i in range(length):
        for j in range(length - i + 1):
            print(end=" ")

        row = []
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            nCr = factorial(i) // (factorial(j) * factorial(i - j))
            mod = rule(nCr)
            row.append(mod)
            print(mod, end=" ")
        print()

        full.append(row)
    return full


def try_one():
    return pascal(rule=lambda x: round(log(x)), length=30)


def try_two():
    length = 200
    a = pascal(rule=lambda x: round(log(x)), length=length)
    new = []
    for b in a:
        new.append(([0] * (length - len(b))) + b)

    sns.heatmap(new)
    plt.show()
    return new


def try_three():
    length = 200
    a = pascal(rule=lambda x: round(log(x)), length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_four():
    length = 10
    rule = lambda x: x

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_five():
    length = 200
    rule = lambda x: round(log(x, 100))

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_six():
    length = 600
    rule = lambda x: round(log(x, 10000))

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_seven():
    length = 200
    rule = lambda x: x % 3

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_eight():
    length = 200
    rule = lambda x: x % 2

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_nine():
    length = 200
    rule = lambda x: math.sin(x)

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_ten():
    length = 200
    rule = lambda x: abs(math.sin(x) ** math.cos(x))

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_eleven():
    length = 200
    rule = lambda x: round(max(math.sin(x), math.cos(x)))

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_twelve():
    length = 30
    rule = lambda x: round(log(x))

    a = pascal(rule=rule, length=length)

    for b in a:
        print(sum(b))


def try_thirteen():
    length = 20
    rule = lambda x: math.gcd(x) / max(1, log(x))

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        print(cur)
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_sixteen():
    length = 200
    rule = lambda x: 1 / x if x % 6 else 0

    a = pascal(rule=rule, length=length)
    new = []
    for b in a:
        before = [0] * (floor(length - len(b) / 2))
        after = [0] * (ceil(length - len(b) / 2))
        cur = before + b + after
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_nineteen():
    length = 1000
    rule_a = lambda x: 1 if x % 6 else 0
    rule_b = lambda x: 1 if x % 11 else 0

    a = pascal(rule=rule_a, length=length)
    b = pascal(rule=rule_b, length=length)

    c = []
    for x, y in zip(a, b):
        h = []
        for j, k in zip(x, y):
            h.append(abs(j - k))
        c.append(h)

    # print(c)

    new = []
    for p in c:
        before = [0] * (floor(length - len(p) / 2))
        after = [0] * (ceil(length - len(p) / 2))
        cur = before + p + after
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def try_twenty():
    length = 1000
    rule_a = lambda x: 1 if x % 13 else 0
    rule_b = lambda x: 1 if x % 11 else 0

    a = pascal(rule=rule_a, length=length)
    b = pascal(rule=rule_b, length=length)

    c = []
    for x, y in zip(a, b):
        h = []
        for j, k in zip(x, y):
            h.append(abs(j - k))
        c.append(h)

    # print(c)

    new = []
    for p in c:
        before = [0] * (floor(length - len(p) / 2))
        after = [0] * (ceil(length - len(p) / 2))
        cur = before + p + after
        new.append(cur)

    sns.heatmap(new)
    plt.show()
    return new


def to_image(array):
    w = h = len(array) * 2
    data = np.zeros((h, w, 3), dtype=np.uint8)

    for x, row in enumerate(array):
        for y, column in enumerate(array[x]):
            data[x, y] = (210, 200, 200) if column else 0

    img = Image.fromarray(data, "RGB")
    img.save("twenty.png")


if __name__ == "__main__":
    out = try_twenty()
    to_image(out)
