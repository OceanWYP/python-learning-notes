#[]、[:]  索引、切片
# **   幂
# ~、+、-  按位取反、正号、负号
#*、/、%、//  乘、除、模、整除
# >>、<< 右移、左移
#<=、<、>、>=  小于等于、小于、大于、大于等于
# ==、!=  等于、不等于
#is、is not  身份运算符
#in、 not in 成员运算符
#not、or、and 逻辑运算符
#=、+=、-=、*=、/=、%=、//=、**=、&=、|=、^=、>>=、<<=  赋值运算符
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241

#赋值运算符
#赋值运算符应该是最为常见的运算符，它的作用是将右边的值赋给左边的变量。
"""
赋值运算符和复合赋值运算符

version：3.10
Autor: 吴慎之
"""
a = 10
b = 3
a += b      #相当于：a = a + b
a *= a + 2  #相当于：a = a * (a + 2)
print(a) 

"""
海象运算符

Version: 3.10
Author: 吴慎之
"""
# SyntaxError: invalid syntax
# print((a = 10))
# 海象运算符
print((a := 10))  # 10
print(a)          # 10

"""
比较运算符和逻辑运算符的使用

Version: 3.0
Author: 吴慎之
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False

######运算符和表达式应用######
"""
例子1：将华氏温度转换为摄氏温度
"""
f = float(input('请输入华氏温度：')) #input函数用于从键盘接收用户输入，将输入的字符串转化为float浮点型
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))#%.1f是字符串格式化中的“小数点控制符”，让输出结果只显示一位小数
#%：格式化标记符  .:小数点前的控制  1：保留1位小数 f：浮点数类型，这是一个小数，不是整数
# %d	%.0f	37（整数，无小数）
# %f	%.2f	37.00（保留 2 位小数）
# %s	%s	字符串（如 37.0）
# %0.1f	%.1f	37.0（同 %.1f）
#优化代码：
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')  # 用 f-string 替代 % 格式化

"""
例子2：计算圆的周长和面积
"""
radius = float(input('请输入圆的半径：'))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长： %.2f' %perimeter)
print('面积： %.2f' % area)

###优化引入数学math模块，使用pi
import math

radius = float(input('请输入圆的半径: '))  # 输入: 5.5
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
print(f'{area = :.2f}')       # 输出：area = 95.03

###判断闰年
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')#and和or运算符将三个条件组装在一起，前两个条件要同时满足，第三个条件跟前两个条件的组合只需满足其中之一。

