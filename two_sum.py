"""This is a subroutine where from a given array of integers num_list one can find a pair of numbers
whose sum is equal to a given integer nsum"""
def sum_of_two(num_list, nsum):
    #define a list called result which will store the indices
    result=[]
    for i, num in enumerate(num_list): #this loop runs over all the elemets in the list as well as their indices
        req_num=nsum-num # define a number which gives a difference b/w nsum and num
        if req_num in num_list:
            #if this req_num is there in num_list then store its index in j
            j=num_list.index(req_num)
            if i!=j and i<j:
                result.append((j,i)) #keeps on adding the pair of indices
    return result #return the list result

num_list=[2,3,7,11,1,6,15]
nsum=9
print(sum_of_two(num_list,nsum))
