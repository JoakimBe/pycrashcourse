num1 = 11
num2 = 12

print("hej " + str(num1) + " på " + str(num2) + " dig ")
print("hej %s på %s dig" % (num1, num2))
print("hej {0} på {1} dig".format(num1, num2))
print("hej {num1} på {num2} dig".format(num1=num1, num2=num2))