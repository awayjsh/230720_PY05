# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(string):

    ans = []

    for i in range (len(string)) :

        ans.append(string[-(i+1)])

    return ''.join(map(str,ans))

result = reverse_string("Hello, World!")
print(result)
