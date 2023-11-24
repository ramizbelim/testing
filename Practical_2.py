start_number = int(input("Enter the start number :"))
end_number = int(input("Enter the end number(range) :"))
count = 0
for number in range(start_number, end_number + 1):
    number_l = list(str(number))
    if len(number_l) == len(set(number_l)):
        count +=1
print(count)


