# ws_5_2.py

# 아래 함수를 수정하시오.
def remove_duplicates(old_lst):
    
    new_lst = []
    
    new_lst = list(set(old_lst))

    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
