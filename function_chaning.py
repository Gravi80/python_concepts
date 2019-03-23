from functools import reduce


def increment(num):
    return num + 1


def double(num):
    return num ** 2


func_chain = [increment, double]
input_num = 2

if __name__ == '__main__':
    result = reduce(lambda res, func: func(res), func_chain, input_num)
    print(result)
