str = input()
answer = ''

for i in str:
    if str.isupper():
        answer += i.lower()
    else:
        answer += i.upper()

