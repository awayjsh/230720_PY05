# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(old_tuple):
  
    new_tuple = ()

    sort_list = list(old_tuple)
    sort_list.sort()
    new_tuple = tuple(sort_list)

    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)