##For loop
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myTuple = tuple(myList)

##Octal literals needs a leading 0o to work..
myDict = {'John Doe': '07654...', 'Jane Doe': '07655...', 'Johnny Doe': '07656...'}

##Print lists, tuples etc
# for number in myTuple:
#     print(number)

##Print key, value from a dict
for k, v in myDict.items():
    print("Key: {key}\nValue: {value}\n".format(key=k, value=v))

##While loop
# a = 1
# while a <= 10:
#
#     if a < 10:
#         print("{num}(10)".format(num=a))
#     else:
#         print("{num}(10) DONE".format(num=a))
#
#     a += 1