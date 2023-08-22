# basic events functions for STA 3032 done in python
#The code is pretty basic, as this was done to follow along and practice statistics calculations for studying
#and completing homework
# By Alex Vasta

import numpy
import math
import itertools

# class for operations to be done on sets
#many of the methods in this class were created based on the probablility rules taught during the lecture.
class CalculationSpace():
    def __init__(self, space):
        #current probablility space
        self.space = []

        #current set
        self.currentSet = []

        #Calculations done in this class
        self.calcs = []
        self.currentCalc = 0
        self.lastOperation = ""
        self.operationsPreformed = []

#generators
    def generate_space(self, size):
        for i in range(1, size):
            self.space.append(i)

    def generate_currentset(self,size):
        for i in range(1, size):
            self.currentSet.append(i)

    # Calculates the union of 2 event arrays
    def union(self, A, B):
        final = []
        for num in A:
            final.append(num)
        for num in B:
            if num not in final:
                final.append(num)
        self.currentSet = final
        self.lastOperation = "Union"
        self.operationsPreformed.append(self.lastOperation)
        self.calcs.append(final)
        return final

    # calculates the intersection of 2 given event arrays
    def intersect(self, A, B):
        final = []
        for numa in A:
            if numa in B:
                if numa not in final:
                    final.append(numa)
        self.currentSet = final
        self.lastOperation = "Intersect"
        self.operationsPreformed.append(self.lastOperation)
        self.calcs.append(final)
        return final

    # finds the compliment of an event array given a space
    def compliment(self, set, A):
        final = []
        for num in set:
            if num not in A:
                final.append(num)
        self.currentSet = final
        self.lastOperation = "Compliment"
        self.operationsPreformed.append(self.lastOperation)
        self.calcs.append(final)
        return final

    #The permutation of an object set at a time
    def perm_at_time(self, n, r):
        permn = math.factorial(n)
        permr = math.factorial(n - r)
        final = permn / permr
        self.currentCalc = final
        self.calcs.append(final)
        self.lastOperation = "Permutation at a time"
        self.operationsPreformed.append(self.lastOperation)
        return final

    # works with trying to figure out cells into objects
    def perm_number(self, n1, nk):
        permnk = 1
        permn1 = math.factorial(n1)
        for n in nk:
            permnk = permnk * math.factorial(n)
        final = permn1 / permnk
        self.currentCalc = final
        self.calcs.append(final)
        self.lastOperation = "Number of permutations"
        self.operationsPreformed.append(self.lastOperation)
        return final

#method for printing a permutation of a specific combination
    def perm_combination(self, n, r):
        permnk = 1
        permn = math.factorial(n)
        permrn = math.factorial(n - r)
        permr = math.factorial(r)
        final = permn / permr * permrn
        self.currentCalc = final
        self.calcs.append(final)
        self.lastOperation = "Combination of permutations"
        self.operationsPreformed.append(self.lastOperation)
        return final

    #prints the order which the calculations where preformed
    def print_calcs(self):
        calcString = ""
        i = 0
        for calc in self.calcs:
            if (i  == 0):
                calcString = " The first calculation preformed was a " + str(self.operationsPreformed[i]) +  " and the result was " + str(self.calcs[i])
            else:
                calcString += "\n The next calculation preformed was a " + str(self.operationsPreformed[i]) +  " and the result was " + str(self.calcs[i])
            i+= 1
        print(calcString)
        return

# the main method
if __name__ == '__main__':

    #test methods to make sure that the above class calculation space is working
    space = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    A = [2, 4, 6, 8, 10, 12]
    B = [3, 6, 9, 12]
    N = ["M1","M2","F1","F2"]
    someParse = []
    S = []
    #calcS = CalculationSpace(space)

    #calcS.union(A, B)
    #calcS.intersect(A, B)
    #calcS.compliment(space, A)
    #print(2 * 4 * 3 * 5)

    # permutation main exectution
    nk = [3, 2, 2]
    #calcS.perm_number(7, nk)
    #calcS.print_calcs()


#the elements of sample space S will contain all possible permutations of male and female applicants, which will be:
    for L in range(4):
        for subset in itertools.permutations(N, L):
            if (len(subset) == 2):
                S.append(subset)
    print("THIS IS THE SET: " + str(S))

    #Event A’s set is calculated by removing all elements of the space that start with a female taking the place of a male.
    #This can be calculated by using the following python code to check if the first candidate is a male in the space established in part a:
    A = []
    for canidates in S:
        if 'M' in canidates[0]:
            A.append(canidates)
    print("THIS IS A: " + str(A))

    #Event B’s set is calculated by removing any elements within the space that do not have at least one male.
    #This can be calculated with the following python code that will check if only one male is in the element before appending to the set B:
    B = []
    for canidates in S:
        males = 0
        for canidate in canidates:
            if 'M' in canidate:
                males +=1
        if males == 1:
            B.append(canidates)
    print("THIS IS B: " + str(B))

    x = 2
    f = ((math.pow(6,x))/(math.factorial(x)))
    f = (math.pow(math.e,-6) * f)
    print("This is the answer to part b of problem 4: " + str(f))

    i  =0
    j = 0
    k = 0
    l = 0
    x = [0,1,2,3]
    y = [0,1,2]
    probDist = []
    probA = 0
    randomSampleP = math.comb(8,4)
    print(math.comb(8,4))
    for i in x:
        for j in y:
            if (k != 0) and (k != 11):
                if (i + j <= 2):
                    probDist.append((math.comb(3,i) * math.comb(2,j)* math.comb(3,abs(4-i-j))) / randomSampleP)
                    print("x = " + str(i) + " y = " + str(j) + " Probability this occurs = " + str(probDist[l]))
                    l += 1
            k+=1
    i  =0
    j = 0
    n = 0
    k = 0
    x = [0,1,2,3]
    y = [0,1,2]
    sumXs = 0
    sumYs = 0
    sumXY = 0
    sumX = 0
    sumY = 0
    for i in x:
        for j in y:
            if (k != 0) and (k != 11):
                sumXs += i * i
                sumYs += j * j
                sumXY += i * j
                sumX += i
                sumY += j
                n += 1
            k+= 1
    print(n)
    corrDenom = (n * (sumXY)) - (sumX * sumY)
    corrNum = math.sqrt(((n * sumXs) - sumXs) * ((n * sumYs) - sumYs))
    correlation = corrDenom/corrNum
    print("The correlation coefficient: " + str(correlation))

    thing = 0.12857142857142856+ 0.2571428571428571+ 0.04285714285714286
    thing = 1/thing
    thing =  2.3333333333333335*(0.04285714285714286)
    print("THING IS " + str(thing))
    probA = math.fsum(probDist)
    print("the probability of A is: " + str(probA))



    #to find the set of elements C, we would find the compliment of B with respect to the space S. This is calculated through the following python code:
    calcS = CalculationSpace(space)
    C = calcS.compliment(S,B)
    print("THIS IS C: " + str(C))
    print("THE UNION OF A AND B " + str(calcS.union(A,B)))
    print("THE INTERSECT OF A AND B: " + str(calcS.intersect(A,B)))

    #misc calculations done during the lecture
    print(str(0.78/0.83))
    print(str(0.78/0.82))
