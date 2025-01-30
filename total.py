def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]

    # print(initial,' |initial \n')
    # print(number,'|number \n')
    # print(numbers,'|numbers \n')
    # print(keywords,'|keywords \n')
    # print(key,'|key \n')
    return count
    
# total(10, 1, 2, 3, vegetables=50, fruits=100)

print(total(10, 1, 2, 3, vegetables=50, fruits=100))
