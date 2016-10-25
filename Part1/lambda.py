def apply(f, num1, num2):
    print(f(num1, num2))

subtraction = lambda num1, num2: num1 - num2
adition = lambda num1, num2: num1 + num2


apply(subtraction, 10, 5)


def summarize(num1, num2):
    return num1+num2(10)

summary = summarize(10, lambda num2: num2*50)
print(summary)


