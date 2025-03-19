import math

# 获取用户输入
a = int(input("请输入整数 a: "))
b = int(input("请输入整数 b: "))
c = int(input("请输入整数 c: "))

# 计算判别式
discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    # 计算实根
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    # 按从大到小排序
    roots = [root1, root2]
    roots.sort(reverse=True)
    print(f"{roots[0]:.2f},{roots[1]:.2f}")
else:
    print("无实根")
    