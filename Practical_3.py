# given_list = [33, 48, 24, 64, 824, 123, 451, 154, 234, 114, 412]
user_input = int(input("Enter the length you want for list :"))
list_from_user = []
for i in range(user_input):
    x = int(input("Enter element of list :"))
    list_from_user.append(x)
#Sum of the elements of number
def sum_of_element(list):
    sum_of_element = []
    for i in range(len(list)):
        for element in list:
            sum = 0
            for element_of_element in str(element):
                sum =sum + int(element_of_element)
            if sum%2==0 and sum%4==0:
                sum_of_element.append(element)
        break
    return sum_of_element
print(sum_of_element(list_from_user))

