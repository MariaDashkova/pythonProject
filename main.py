# 1.
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему
from typing import List, Tuple


def me(words):
    if len(words) != 0:
        count = 0
        sp = words.split()
        for st in sp:
            if (len(st) > 2) & (st[0] == st[len(st) - 1]):
                count = count + 1
        return count
    return ""


# 2.
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
    xlist = [x for x in words if x[0] == 'x']
    list = [x for x in words if x[0] != 'x']
    xlist.sort()
    list.sort()
    return xlist + list


# 3.
# Вх: список непустых кортежей,
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

# sorter(words: List[Tuple[int]]) -> List[Tuple[int]]:
def sorter(words):
    words.sort(key=lambda i: i[1])
    return words


def test(res, expt):
    print('returns: ' + str(res) + '\n' + 'supposed to return: ' + str(expt))
    if str(str(res)) == expt:
        print('ОК'+ '\n')
    else:
        print('FAIL' + '\n')


def main():
    test(me('tam tut mem'), '2')
    test(fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']), "['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']")
    test(sorter([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), "[(2, 2), (1, 3), (3, 4, 5), (1, 7)]")


if __name__ == '__main__':
    main()
    print("Everything passed")
