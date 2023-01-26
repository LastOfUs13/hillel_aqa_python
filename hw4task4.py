my_list = ["FirstItem", "FriendsList", "MyTuple"]
new_str = str(my_list)
low_str = new_str.casefold()
str_with_line_1 = low_str.replace('firstitem', "first_item")
str_with_line_2 = str_with_line_1.replace("friendslist", "friends_list")
str_with_line_3 = str_with_line_2.replace("mytuple", "my_tuple")
print(str_with_line_3)