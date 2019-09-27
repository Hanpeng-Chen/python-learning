#########  一个except子句可以同时处理多个异常  #########
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except (ValueError, IndexError) as err:
    print('Error: {}'.format(err))
    
print('continue')



######  一个 try 语句可能包含多个except子句 ######
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))

print('continue')




######  最后一个except block，声明其处理的异常类型是Exception   ######
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other Error: {}'.format(err))

print('continue')


##########  最后一个except子句可以忽略异常的名称  ###########
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except:
    print('Other error')

print('continue')


#######  常见的应用场景如：读取文件  ########
import sys
try:
    f = open('file.txt', 'r')
    .... # some data processing
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    f.close()



#######   else子句   #######
try:
    s = input('please enter two numbers separated by ",":')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
except ValueError as err:
    print('Value Error: {}'.format(err))
else:
    print('in else')



########异常处理还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常##########
def this_fails():
    x = 1/0
   
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)