# 编写函数，判断输入参数字符串是否为邮箱地址，
# 检验条件为：字符串中间用@分隔，末尾是.com或者.net（

arr1 = input('请输入字符串邮箱:')
arr2 = 'com'
if arr2 in arr1:
    print('邮箱正确')
else:
    print('邮箱不正确请重新输入')