# ###分支结构###

# # # if、elif、else
# # #例子：
# # height = float(input('身高(cm): '))
# # weight = float(input('体重(kg): '))
# # bmi = weight / (height / 100) ** 2
# # print(f'{bmi = :.1f}') #{}：是专门用于f-string里包裹表达式，作用是告诉python，这里药计算并插入一个值
# # if 18.5 <= bmi <24:
# #     print('你的身材很棒')

# # # ###！！！保持相同的缩进，就属于同一个代码块，相当于一个执行的整体，通常缩进4个空格。

# # # #优化，创造分支，包含并回答其他的可能性。

# # # height = float(input("身高(cm):"))
# # # weight = float(input('体重(kg):'))
# # # bmi = weight / (height / 100) ** 2
# # # print(f"{bmi = :.1f}")
# # # if 18.5 <= bmi <24:
# # #     print('你的身材很棒')
# # # else:
# # #     print('你的身材不够标准')

# # # ##创造更多的分支##
# # # height = float(input('身高(cm):'))
# # # weight = float(input('体重(kg)：'))
# # # bmi = weight / (height / 100) ** 2
# # # print(f'{bmi = :.1f}')
# # # if bmi < 18.5:
# # #     print('你的体重过轻！')
# # # elif bmi < 24:
# # #     print('你的身材很棒！')
# # # elif bmi < 27:
# # #     print('你的体重过重！')
# # # elif bmi < 30:
# # #     print('你已轻度肥胖！')
# # # elif bmi < 35:
# # #     print('你已中度肥胖！')
# # # else:
# # #     print('你已重度肥胖！')


# # # 使用match和case构造分支结构
# # status_code = int(input('响应状态码：')) #input():作用是暂停程序运行，等待用户在终端输入内容，然后将输入的内容以字符串形式返回
# # if status_code == 400:
# #     description = 'Bad Request'
# # elif status_code == 401:
# #     description = 'Unauthorized'
# # elif status_code == 403:
# #     description = 'Forbidden'
# # elif status_code == 404:
# #     description = 'Not Found'
# # elif status_code == 405:
# #     description = 'Method Not Allowed'
# # elif status_code == 418:
# #     description = 'I am a teapot'
# # elif status_code == 429:
# #     description = 'Too many requests'
# # else:
# #     description = 'Unknown status Code'
# # print('状态码描述:', description)

# # 使用match-case语法实现：
# status_code = int(input('响应状态码：'))
# match status_code:
#     case 400: description = 'bad request'
#     case 401: description = 'unauthorized'
#     case 403: description = 'fobidden'
#     case 404: description = 'not found'
#     case 405: description = 'method not allowed'
#     case 418: description = 'i am a teapot'
#     case 429: description = 'too many request'
#     case _: description ='unknown status code'
# print('状态码描述：',description)
# #带有_的case语句在代码中起到通配符的作用，如果前面的分支都没有匹配上，代码就会来到case _
# #case _的是可选的，并非每种分支结构都要给出通配符选项。如果分支中出现了case _，它只能放在分支结构的最后面，如果它的后面还有其他的分支，那么这些分支将是不可达的。

# #match-case高级玩法：合并
# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400 | 405: description = 'Invalid Request'
#     case 401 | 403 | 404: description = 'Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)

# #例子：
# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print (f'{y =}') #f是f-string(格式化字符串)的前缀，作用是让字符串支持直接嵌入变量和表达式。

#尝试使用match-case来写
x = float(input('x = '))
match x:
    case _ if x> 1: #通配符_:作用是匹配任何值，但不绑定变量；忽略 x 的具体值，只检查 x > 1 是否成立
        y = 3 * x - 5
    case _ if x >= -1:
        y = x + 2
    case _ : #匹配所有剩余情况（自动覆盖 x < -1）
        y = 5 * x + 3
print(f'{y =}')


