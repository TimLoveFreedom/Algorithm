from 栈.stack import Stack

__author__ = 'jellyzhang'
'''
括号匹配
'''
str1='((()('
str2='()()()(())'

stack=Stack()
for s in str2:
    if s=='(':
        stack.push(s)
    elif s==')':
        if stack.isEmpty():
            print('不匹配')
            break
        else:
            stack.pop()
if stack.isEmpty():
    print('匹配')
else:
    print('不匹配')
