"""
while 条件:
    条件成立要重复执行的代码
    ......
"""

# 需求：重复打印5次媳妇儿，我错了 -- 1， 2， 3， 4， 5  6X -- 数据表示循环的次数 -- 第一次是1，最后依次5
# 1 + 1 + 1....
i = 1
while i <= 5:
    print('媳妇儿，我错了')
    i += 1  # i = i + 1

i = 0
while i < 5:
    print(f"i={i}")
    i += 1







