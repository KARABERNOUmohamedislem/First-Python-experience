

def upper_and_reverse (phrase):
    a=len(phrase)
    result=''
    phrase1=phrase.upper()
    for i in range(0,a):
        result=result + phrase1[a-i-1]

    print(result)

y=input('type a sentence : ')
upper_and_reverse(y)

