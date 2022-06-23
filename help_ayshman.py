'''PROBLEM STATEMENT
A pharmacist sells two types of masks with prices 'x' and 'y' respectively.
Owner of the store wants to know the minimum possible amount 'z' such that any amount greater than or equal to 'z' can be earned by the owner by selling any number of the masks in any order. If it's impossible to do with the given x and y, print "IMPOSSIBLE" in that case.
You being Ayushman's good friend, help him solve this.

For more clear explanation, consider the following test case.

Example - 
1) Let x be 4 and y be 5
Amount 1, 2, 3 Not Possible in any way.
4 = 4*1 + 5*0
5 = 4*0 + 5*1
6, 7 Not Possible in any way.
8 = 4*2 + 5*0
9 = 4*1 + 5*1
10 = 4*0 + 5*2
11 Not Possible in any way.
12 = 4*3 + 5*0
13 = 4*2 + 5*1
14 = 4*1 + 5*2
15 = 4*3 + 3*1
16 = 4*4 + 5*0
17 = 4*3 + 5*1
.
.
So it can be seen that, from 12 onwards, we can represent any amount by selling any number of Masks.
Therefore our answer for this case is 12.

2) Let x be 22 and y be 4
Answer for this case is "IMPOSSIBLE"


CONSTRAINTS - 
1 <= T <= 10
1 <= x <= 1e8
1 <= y <= 1e8

INPUT FORMAT - 
First line contains the integer T, the number of test cases.
Next each T lines contains two space separated positive integers 'x' and 'y' respectively.

OUTPUT FORMAT - 
Print the required amount 'z' if it's possible to do so. Otherwise print "IMPOSSIBLE"
'''

#Code
#Algo: we will get the start no. of A.P is by formula --> x*y - (x+y) + 1)
#      Checking L.C.M is multiply of two nums

n1=int(input())
def lcm(x, y):
    from fractions import gcd
    return x * y // gcd(x, y)
for i in range( n1):
 x, y = map(  int, input().split())
 if  lcm(x,y) == x*y:
  print( (x*y - (x+y) + 1))
 else:
  print( "IMPOSSIBLE")