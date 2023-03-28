#Mendel's first law of inheritance (law of segregation)
#Input: Three positive integers k, m, and n, representing a population containing k + m + n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive and pht number (1 dominant phenotype or 0 for recessive phenotype).
#Output: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (if pht = 1 and thus displaying the dominant phenotype) or recessive phnotype (if pht = 0), assuming that any two organisms can mate.


from math import *

inp_list = []

n = 3
#Enter k, m, n numbers
#k (first input) individuals are homozygous dominant for a factor
#m (second input) individuals are heterozygous for a factor
#n (third input) individuals are homozygous recessive for a factor
for i in range(0, n):
    ele = int(input("Enter the numbers in ordered way (k then m then n): "))
    inp_list.append(ele)

def model(inp_list,out):
    k = int(inp_list[0])
    m = int(inp_list[1])
    n = int(inp_list[2])
    tot = k + m + n                   #total organisms
    tot_opt = comb(tot,2)
    a = {"AA" : 1}
    b = {"BB": 1}
    h = {"AA":0.25, "AB": 0.5, "BB": 0.25}
    ab = {"AB":1}
    ah = {"AA": 0.5, "AB": 0.5}
    bh = {"BB": 0.5, "AB":0.5}

    list = []
    dom = []
    rec = []

    for i in range(comb(k,2)):
        list.append(a)
    for i in range(comb(m,2)):
        list.append(h)
    for i in range(comb(n,2)):
        list.append(b)
    for i in range(k*m):
        list.append(ah)
    for i in range(k*n):
        list.append(ab)
    for i in range(m*n):
        list.append(bh)

    for poss in list:
        for gt in poss:
            if "A" in gt:
                dom.append(poss[gt]*(1/tot_opt))
            elif "BB" in gt:
                rec.append(poss[gt]*(1/tot_opt))

    if out == 1:                                 #1 for dominant phenotype
        return round(sum(dom), 5)
    elif out == 0:                               #0 for recessive phenotype
        return round(sum(rec), 5)
    else:
        return "Please, choose only 1 or 0"

pht = int(input("Enter 1 for the probability of dominant phenotype and 0 for recessive phenotype: "))
print("The probability is: ", model(inp_list,pht))