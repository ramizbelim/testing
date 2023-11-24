user_string = " Tom, Tony, tony@Stark, alfred254, Tony stark, Edward, tom$323, Nigam, frank, Francis, nigam Gupta "
# user_string = input("Enter a sentence : ")
def practical_1(sentence):
    sentence_strip = sentence.strip()
    punc = 'aeiou,'
    result = ""
    for ele in sentence_strip:
        if ele not in punc:
            result += ele
    string = [ele for ele in result.strip().split() if ele.isalnum()]
    res = " ".join(string)
    count_digit = 0
    for digit in res:
        if digit.isdigit():
            count_digit +=1
    return count_digit
print(practical_1(user_string))



