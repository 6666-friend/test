abc = int(input("请输入数字:"))
ab = int(input("请输入第二个数字:"))
a = input("请输入要进行的运算，例如+，-，*，/")

if a == "+":
    abcd = abc + ab
elif a == "-":
    abcd = abc - ab
elif a == "*":
    abcd = abc * ab
elif a == "/":
    abcd = abc / ab
else:
    print("无效的运算符")
    exit()  # 如果无效运算符，退出程序

print("计算完毕，结果为：", abcd)

