# Comma Code

spam = ['apples','bananas','tofu']
spam = []

def comma(list):
    if len(list) == 0:
        print('There is nothing in this list.')
    else:
        for i in range(len(list)-2):
            print(list[i], end=", ")
        print(list[-2] + ' and ' + list[-1])

comma(spam)
