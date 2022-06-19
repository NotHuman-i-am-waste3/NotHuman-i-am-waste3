'''
Program name - DEPENDENCY TREE
Concept used - Recursion 

What is given - Given an aplhabets each having connectivty which is like inhertinace 

RELATED TO:
    given elemnts of parents 
    given a letter , find the possible all connection of that letter

GIVEN :

A B

A C

B E

B F

B G

D H

For example, in the above tree, if F is given then the dependencies are B and A.

sample output:
3
A B
B C
C D
D

Here D is connected to all letter as A B C is printed 
WARNING !!
GIVE NEAT RELATIONS IN INPUT OR ELSE PROGARAMM WILL SHOW BECAUSE IT CREATS LOOP HOLE FOR RECURSION

Here's the code <3
'''
n=int(input())
l=[list(map(str,input().split())) for i in range(n)]
a=input();ans=[]
def comp(a):
 opr=[]
 for i in l:
    if i[-1]==a: 
        opr.append(i)
        ans.append(i[0])
        comp(i[0])
 if len(opr)==0:      #  CHECKING FOR THE END ALPHABET HAVING NO CONNECTIONS
        print(*ans)
comp(a)  # Creating Base recursion 








