##Strings
oneLineString = "Detta är en sträng"
#print(oneLineString)

multiLineString = """
Hej detta ären
flera linjer
lång sträng
"""
#print(multiLineString)

##Numbers
aNumber = 45
aNumber2 = 1.3

# print(aNumber, aNumber2, ((aNumber+aNumber2)-15.7)+100)

##Number and string combo
# print("Some simple math!: "+str(((aNumber+aNumber2)-15.7)+100))
# print("Some simple math!: {calc} ".format(calc=((aNumber+aNumber2)-15.7)+100))

##Boolean, example usage
isActive = True
isActive = False

# if isActive:
#     print("isActive is: {isActive}, changing value to False".format(isActive=isActive))
#     isActive = False
# else:
#     print("isActive is: {isActive}, changing value to True".format(isActive=isActive))
#     isActive = True
#
# print("isActive is changed to {isActive}".format(isActive=isActive))

##Lists
aList = [1, 2, "Kalle", [5, 6, 7], True, 7.8, {'value1': 1, 'value2': 'En sträng'}]

# for listItem in aList:
#     try:
#         if 6 in listItem:
#             print(listItem)
#     except:
#         pass

##Tuple
aTuple = (1, 2, 3)
aList.append(1000)
# print(aList, aTuple)

##Sets
print(set("my name is Eric and Eric is my name".split()))
print(sorted(set("my name is Eric and Eric is my name".split())))