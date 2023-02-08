def count_list(list_1):
    c = []
    for i in list_1:
        if type(i) is list:
            c.append(i)
    return len(c)
# c_1 = 0
a_1 = [['f', 'k']]
b = [[1], [2]]
# p = sum([c_1+1 for i in a if type(i) is list])
# k = len(list(filter(lambda x: type(x) is list, a)))
lst = [1, [], [1, ['f', 'k']], 5, 7, 1, 2, 3, [[['1', ['a', 'f']]]]]
while True:
    lst_1 = []
    for i in lst:
        if type(i) is not list:
            lst_1.append(i)
        else:
            for j in i:
                lst_1.append(j)

    x = list(filter(lambda x: type(x) is list, lst_1))
    if count_list(lst_1) == 1 and len(x) == 1 and count_list(x[0]) == 0:
        print(*x[0])
        break
    else:
        lst = lst_1