#1 find_max


def find_max(numbers):
    num = numbers[0]
    for i in numbers:
        if i > num:
            num = 
    return num


print(find_max([1, 2, 4, 5]) ); # should print 5
print(find_max([5, 2, 7, 1, 6]) ) # should print 7


# ---

def find_position(numbers, target):
    num = ""
    for i in range(len(numbers)):
        if numbers[i] == target:
            num = i
            break
    if num != "":
        return num
    else:
        return -1


print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1


# ---

def count(input):
# your code here
    result = {}
    for i in input:
        result[i] = result.get(i,0)+1
    return result


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

# ---

def group_by_key(input):
# your code here
    result={}
    for i in input:
        k = i["key"]
        v = i["value"]
        result[k] = result.get(k, 0) + v
    return result


input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
