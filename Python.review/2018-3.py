"""2018年Python课程期末考试试题及答案    2019年12月27日"""import redef isLeapYear(y):    # 判断闰年函数    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:        return True    else:        return Falsedef func1(y, m, d):    """    1.	给定用于表示年、月、日的3个整数y、m和d，判定该日期是该年的第几天。    输入条件	输入用于表示日期（年、月、日）的3个正整数y、m和d，            肯定是正整数，但是否属于合法的日期数据未知。    输出要求	返回值为整型，具体定义如下：            1)	如所给日期数据不合法，返回-1            2)	如所给日期数据合法，则返回该日期是该年的第几天。                以2019-1-1为例，该日期是2019年的第1天，则返回1    """    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}    if isLeapYear(y):        month_days[2] = 29    if m > 12 or d > month_days[m]:        return -1    return sum(list(month_days.values())[0:m - 1]) + ddef func2(m, n):    """    2.	已知每只鸡有2只脚，每只兔子有4只脚，求解鸡兔同笼问题。        给定鸡和兔子的头的总数m和脚的总数n。求鸡和兔子的数量    :param m: int 头的总数    :param n: int 脚的总数    :return: 鸡和兔子的数量(int) -> tuple    要求:如果m和n中任何一个小于0，返回None         如任何一个解不是整数，或任何一个解小于0，返回None    """    # 或者穷举    if m * n < 0:        return None    x = (4 * m - n) / 2    y = (n - 2 * m) / 2    if x * y < 0 or int(x) != x or int(y) != y:        return None    return int(x), int(y)def func3(lst):    """    3.	判定一个整数列表里的元素排序后能否构成等差数列。    输出要求	如果列表为空列表或只有一个元素，返回None            如果列表有两个元素，返回True    :param lst: list    :return: None or bool    """    if len(lst) <= 1:        return None    if len(lst) == 2:        return True    lst = sorted(lst)    d = lst[1] - lst[0]    for i in range(1, len(lst) - 1):        t = lst[i + 1] - lst[i]        if t != d:            return False    return Truedef func4(lst):    """    4.	计算并返回整数列表的中位数。中位数的含义：对于一个有序的数列，        排列位置位于整个列表中间的那个元素的值即为中位数。        如果数列有偶数个值，取最中间的两个数值的平均数作为中位数。    :param lst: a list    :return: 中位数 -> int    """    if len(lst) == 0:        return None    if not all(map(lambda x: isinstance(x, int), lst)):        return None    lst = sorted(lst)    if len(lst) % 2 != 0:        mid = lst[len(lst) // 2]    else:        mid = sum(lst[(len(lst) // 2) - 1:(len(lst) // 2) + 1]) / 2    return int(mid)def func5(sentence):    """    5.	输入一个包含3到11个单词的字符串，单词与单词之间用空格分开，        其中的单词一定是0-9数字的英文单词（单词的字母可能大写也可能小写）        请编写程序将其转换为阿拉伯数字的字符串。    """    sentence = sentence.split()    if len(sentence) not in range(3, 12):        return None    tran = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}    res = []    for number in map(lambda x: x.lower(), sentence):        res.append(tran[number])    return ''.join(res)def func6(a, b, c, d):    """    6.	求集合s = {x / y | a <= x <= b, c <= y <= d}中元素的个数。    :param: 整数a, b, c, d满足1 <= a <= b <= 100, 1 <= c <= d <= 100    :return: 个数 int    """    return len({x / y for x in range(a, b + 1)                for y in range(c, d + 1)})def func7(s1, s2, n):    """    7.	输入两个字符串参数s1, s2（均不为空字符串），和一个非零正整数n。        请按照如下规则将字符串s2插入到s1中，并返回生成的字符串：        1)	s1中每隔n个字符，插入一次s2        2)	如果最后一次不足n个字符，则先用空格符号补全到n个字符，然后插入一次s2    :param s1, s2: str 不为空    :param n: 非零正整数 int    :return: 结果字符串 str    """    # 反思：字符串切片，range对象有步长    lst = [s1[i:i + n] for i in range(0, len(s1), n)]    lst[-1] += ' ' * (n - len(lst[-1]))    return s2.join(lst) + s2def rep(m):    # m代表本轮找到的match对象    s = m.group(1).upper()    return ''.join(('[', s, '-', str(len(s)), ']'))def func8(sentence):    """    8.	给定一个字符串，找出其中“<tag>”形式的标签片段        并替换成“[TAG-len]”形式的片段        其中tag是由字母、数字和下划线构成可变的标签文本        TAG是将tag中的英文字母全部转换成大写字母后的形式        len是TAG的长度，详见测试用例。    :param sentence: str 不包含中文。字符串中可替换部分可能出现0次或多次    :return: str 返回经过替换的字符串。如没有需要替换的内容，则原样返回    """    pattern = re.compile(r'<(\w+)>')  # 子模式    # 每一次找到的match对象作为实参调用rep函数    # 将每一次rep的返回值作为替换值去替换sentence    return pattern.sub(rep, sentence)def my_func8(sentence):    # 重复造轮子    pattern = re.compile(r'<(\w+)>')    obj = pattern.search(sentence)    while obj:        st = obj.start()        en = obj.end()        result = obj.group(1).upper()        TAG = ''.join(('[', result, '-', str(len(result)), ']'))        sentence = ''.join([sentence[:st], TAG, sentence[en:]])        obj = pattern.search(sentence)    return sentenceif __name__ == "__main__":    """ 测试用例 """    print(func1(2019, 3, 1))  # 60    print(func1(2019, 2, 29))  # -1    print(func1(2016, 2, 29))  # 60    print(func1(2019, 12, 31))  # 365    print(func1(2020, 12, 31))  # 366    print(func2(35, 110))  # (15, 20)    print(func2(35, 111))  # None    print(func2(0, 0))  # (0, 0)    print(func2(100, 100))  # None    print(func2(-1, 110))  # None    print(func3([1]))  # None    print(func3([19, 2]))  # True    print(func3([19, -1, 100]))  # False    print(func3([33, -7, 3, 13, 43, 53, 23]))  # True    print(func4([1, 3]))  # 2    print(func4([19, [1, 2, 3]]))  # None    print(func4([19, -1, 100]))  # 19    print(func4([19, -1, 1000, 101]))  # 60    print(func5("one one two two three three four"))  # 1122334    print(func5("One One Zero"))  # 110    print(func5("Nine one one"))  # 911    print(func5("one one"))  # None    print(func5("one one two two three three four two two three three four"))  # None    print(func6(1, 10, 1, 1))  # 10    print(func6(1, 10, 1, 10))  # 63    print(func6(10, 10, 1, 10))  # 10    print(func6(1, 1, 1, 2))  # 2    print(func7('abcd', '#', 1))  # result: a#b#c#d#    print(func7('abcd', '##', 2))  # result: ab##cd##    print(func7('abcd', '##', 3))  # result: abc##d  ##    print(func7('abcd', '##', 5))  # result: abcd ##    print(func7('a', '##', 1))  # result: a##    print(func7('abcdefghijkl', '##', 5))  # result: abcde##fghij##kl   ##    print(func8("President <4t>"))  # President [4T-2]    print(func8("hello world"))  # hello world    print(func8("he defended <_abc>, his decision to <43>"))    # he defended [_ABC-4], his decision to [43-2]