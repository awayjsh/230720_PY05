# ws_5_5.py

# 아래 함수를 수정하시오.



def even_elements(my_list):
    
    count = 0
    ans_list = []
    ans_list.extend(my_list)
    length = len(ans_list)

    while count < length:
        
        if ans_list[count] % 2 != 0 :
            
            ans_list.pop(count)

        count = count + 1
        length = len(ans_list)

    return ans_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
