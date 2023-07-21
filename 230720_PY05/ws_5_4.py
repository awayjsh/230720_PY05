# ws_5_4.py

# 아래 함수를 수정하시오.
def capitalize_words(string):

    part_list = list(string.split(" "))

    for i in range(len(part_list)) :

        part_list[i] = part_list[i].capitalize()

    return " ".join((map(str,part_list)))

result = capitalize_words("hello, world!")
print(result)
