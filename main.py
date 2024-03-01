# lst = ["1%","2%","3%"]
# lst1 = []
# for x in lst:
#     y = x.replace("%", "")
#     b = int(y)
#     c = b/100
#     lst1.append(c)
# print(lst1)


# lst = [[1,2,3,4],"name",False]
# rezalt = 0
# for x in lst[0]:
#     rezalt += x
# print(rezalt)

# lst = [[1,2,3,4],"name",False]
# b = 0
# for x in lst:
#     if type(x) == list:
#         for y in x:
#          b += y
# print(b)


# set = {1,2,3,4,5,6,7,1212}
#     print(x)# for x in set:


# person1 = {
#     "Avaz":{
#         "age":15,
#         "address":"Olmaliq"
#     },
#     "Ali":
#         {
#         "age":15,
#         "address":"Oxangaron"
#     }
# }
# r = 0
# for x in person1.values():
#     for y in x.values():
#      if type(y)==int:
#          r+=y

# print(r)

# 1-masala
# a = "A.sinf D.sinf"
# s = a.find("D")
# print(s)

#2-masala
# def count(str):
#     b = "aeiou"
#     resault = 0
#     for x in str:
#         if x in b:
#             resault += 1
#     return resault
#
# print(count("ruxshona"))

#3-masala
# def mapping(harflar):
#     a = {}
#     for x in harflar:
#         a[x] = x.upper()
#     return a
#
# print(mapping(["Hello World"]))

#4-masala
# count_characters = ["###","###","###"]
# x = count_characters.count("###")
# print(x)

# 5_masala
# def mapping(harflar):
#     a = {}
#     for x in harflar:
#         a[x] = x.upper()
#     return a
#
# print(mapping(["a", "v", "y", "z","h","d"]))

# 6-masala
# def calc(lst):
#     resault = {"HARFLAR": 0, "RAQAMLAR":0}
#     for x in lst:
#         if x.isdigit():
#             resault["RAQAMLAR"] += 1
#         elif x.isalpha():
#             resault["HARFLAR"] += 1
#     return resault
#
# print(calc("Menni ismim Ruxshona"))

# 7-masala
# a = input("fam: ")
#
# if a == "Darth Vader":
#     print("Luke, I am your father.")
# elif a == "Leia":
#     print("Luke, I am your sister.")
# elif a == "Han":
#     print("Luke, I am your brother in law.")

# 8-masala
# a = int(input("son: "))
# calc_diff = {"skate": 200, "painting": 200, "shoes": 1 }
# resault = 0
# for x in calc_diff.values():
#     resault += x
#     y = resault-a
# print(y)

# 9-masala
