number_list = input(">>>>输入数组>>>")
int_number_list=[]
replace_number_list = number_list.replace('[','').replace(',', '').replace(']','')
new_number_list= list(replace_number_list)
for num in new_number_list:
    int_number_list.append(int(num))
my_number_list = range(0, len(int_number_list)+1)
for number in my_number_list:
    if number not in int_number_list:
        print(number)
