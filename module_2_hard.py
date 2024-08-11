def get_pairs(first, n):
    result = ""
    for second in range(first + 1, n):
        if n % (first + second) == 0:
            result += f"{first}{second}"
    return result


def get_result(n):
    result = ""
    for first in range(1, n):
        result += get_pairs(first, n)
    return f"{n} - {result}"


for number in range(3, 21):
    result = get_result(number)
    print(result)
