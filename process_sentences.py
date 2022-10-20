sentences = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']
#['thousand devils', 'My name is', 'Room costs', '']


def process(sentences):
    result = [x for x in [' '.join([x for x in  y.split() if x.isalpha()]) for y in sentences]]
    return result


print(process(sentences))
    #result = #YOUR CODE
    #return result
