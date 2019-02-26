# 编写程序，包含try…except…else …finally各个分支内语句,\
# 通过调用测试每个分支运行正确
arr =  input('请输入')
try:
        int(arr)
        print("输入成功")
except:
    print('输入有误')
else:
    print('请输入正确数字')
finally:
    print('111')