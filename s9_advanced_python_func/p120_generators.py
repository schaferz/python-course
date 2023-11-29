def hundred_numbers():
    nums = []
    i = 0

    while i < 100:
        nums.append(i)
        i += 1
    return nums


# print(hundred_numbers())
# print([x * 2 for x in hundred_numbers()])


def hundred_numbers_2():
    i = 0

    while i < 100:
        yield i
        i += 1


g = hundred_numbers_2()
print(next(g))
print(list(g))
