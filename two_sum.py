#May the Force be with you!
"""This is a subroutine where from a given array of integers num_list one can find a pair of numbers
whose sum is equal to a given integer nsum. In this programme we use the concept of Lists."""
def sum_of_two(num_list, nsum):
    #define a list called result which will store the indices
    result=[]
    for i, num in enumerate(num_list): #this loop runs over all the elemets in the list as well as their indices
        req_num=nsum-num # define a number which gives a difference b/w nsum and num
        if req_num in num_list:
            #if this req_num is there in num_list then store its index in j. num_list.index(req_num) is basically index of the re_um from the list num_list.
            j=num_list.index(req_num)
            if i!=j and i<j: # i<j is done to avoid double counting
                result.append((j,i)) #keeps on adding the pair of indices. Append is a useful command to add to a given list 
    return result #return the list result

num_list=[2,3,7,11,1,6,15]
nsum=9
print(sum_of_two(num_list,nsum))
