
def phraseReverse(string):
    list1 = string.split(' ')
    list1.reverse()
    list1 = ' '.join(list1)
    return list1

question = input('Please enter a phrase: ')
answer = phraseReverse(question)
print(answer)