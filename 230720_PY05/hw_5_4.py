# main.py

# 아래 함수를 수정하시오.
def find_min_max(list):
    list.sort()
    ans = (list[0],list[len(list)-1])

    return ans

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)
