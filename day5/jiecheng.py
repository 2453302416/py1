#通过用户输入数字，计算阶乘。（30分）
arr = int(input("请输入数字："))
f=1
sum=0
#循环阶乘
for i in range(1,arr+1):
   f*=i
#输出 最终阶乘的答案
print(f)