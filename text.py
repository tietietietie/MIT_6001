'''
测试tuples是否支持in operator
'''
# my_tuple = (1,2,3,4,5)
# if 1 in my_tuple:
#     print('yes')

'''
test functions as arguments
'''
def func_a():
    print 'inside func_a'
def func_c(z):
    print 'inside func_c'
    return z()
print func_c(func_a) 