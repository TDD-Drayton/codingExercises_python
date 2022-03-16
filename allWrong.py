# Write any import statements here
__author__='TDD-Drayton'

def getWrongAnswers(N: int, C: str) -> str:
    my_list=[]
    A="A"
    B="B"
    my_list[:0]=C
    my_list = list(map(lambda item: item if(item!=A and item!=B) else \
                                        A if(item==B) else B, my_list))
    C=''.join(my_list)

    return C

#Example
#getWrongAnswers(3,ABA)
#getWrongAnswers(5, C: BBBBB)
