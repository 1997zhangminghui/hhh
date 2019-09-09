#1.
#a = float(input('请输入摄氏温度：'))
#b = float(input('请输入华氏温度：'))
#c = a*9/5+32
#d = 5/9 *(b-32)
#print('摄氏温度{}转换为华氏温度为：{}'.format(a,c))
#print('华氏温度{}转换为摄氏温度为：{}'.format(b,d))

#2.
#import math
#length = float(input('输入圆柱体的长：'))
#Radius = float(input('输入圆柱体的半径：'))
#area = math.pi * Radius * Radius 
#Volume = area * length
#print('求圆柱体的底面积:',area)
#print('求圆柱体的体积:',Volume)

#3.
#yingchi = float(input('输入英尺数：'))
#m  = yingchi / 0.305
#print ('输出转化后的米数：',m)

#4.

#M = float(input('水的质量：'))
#intialtemperature = float(input('水的初始温度：'))
#finaltemperature = float(input('水的最终温度：'))
#Q = M * (finaltemperature - intialtemperature) * 4184
#print('计算得将水从初始温度加热到最终温度所需能量为：',Q)


#5.

#chae = float(input('输入差额：'))
#nianlilv = float(input('输入年利率：'))
#lixi = chae * (nianlilv / 1200)
#print('求利息得：',lixi)

#6.

# V1 = float(input ('输入末速度：'))
# V2 = float(input('输出初始速度：'))
# t = float(input('输入占用时间：'))
# a = (V2 - V1) / t
# print('求平均加速度得：',a)

#7.复利值
"""
my = float(input('每月存的钱：'))
yi = my * (1+0.00417) 
er = (my + yi) * (1+0.00417)
san = (my + er) * (1+0.00417)
si = (my + san) * (1+0.00417)
wu = (my + si) * (1+0.00417)
liu = (my + wu) * (1+0.00417)
print('六个月后账户总额： %.3f' % liu)
"""

#8.对一个整数中的各位数字求和
"""
num = int(input('在0~1000之间取一个整数：'))
a = num % 10
b = num // 10
c = b % 10
d = b // 10
sum = (a + c + d)
print('各位数字之和：%d' % sum)
"""
