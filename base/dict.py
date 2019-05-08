import difflib


def dict_use():
    # 多个dict 的合并,key是否为str
    first_map = {2: 21, 7: 81, 4: 41, 5: 51}
    second_map = {3: 31, 6: 61}
    a_map = {'2': 21, '4': 41, '5': 51}
    b_map = {'3': 31, '1': 11}

    # 失败：keyword arguments must be strings
    # cmp(first_map, second_map)
    # 成功：使用update, 针对所以类型的dict
    first_map.update(second_map)
    # print(dict.fromkeys([1, 2, 3], [1, 2]))

    #  调换key与value的值
    d = a_map
    pairs_1 = dict(zip(d.values(), d.keys()))
    pairs_2 = {v: k for k, v in d.items()}
    # key
    pairs_3 = {d.get(k): k for k in d.keys()}
    pairs_4 = {k[1]: k[0] for k in d.items()}
    print('pairs_1', pairs_1)
    print('pairs_2', pairs_2)
    print('pairs_3', pairs_3)
    print('pairs_4', pairs_4)
    a_b_map = dict(a_map, **b_map)
    # 无顺序，随机排序
    print(a_b_map)
    # [(k, a_b_map[k]) for k in sorted(a_b_map.keys())]

#  对于dict的操作
if __name__ == '__main__':
    try:
        seq = difflib.SequenceMatcher(None, 'BIL', 'bil')
        ratio = seq.ratio()
        print(ratio)
        dict_use()
    except Exception as e:
        print(e)