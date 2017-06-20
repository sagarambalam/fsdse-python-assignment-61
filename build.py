def solution(list_of_nums):
    e=0
    o=0
    for i in list_of_nums:
        if(i%2==0):
            e=e+1
        else:
            o=o+1

    return {'ODD': o, 'EVEN': e}

p=solution([1,2,3,4,5])
print p
