#In the first case,23:59:59 there  is good because there is no prime number that leaves a remainder 0
# when it divides all of them.
# Similarly 23:58:59 is also good. Hence the answer is 0:2

#n the second case, there are two bad numbers,23:46:22
# (leaves remainder 0 when divided by 23) and 23:46:46  . There are 816 good numbers. Hence the answer is  2:816


t = int(input())
sslist=[]

def check(h, m, s, lst):
    goodno = 0
    badno = 0
    for i in range(h, 24):
        for j in range(m, 60):
            for k in range(s, 60):
                for number in lst:

                    if k % number == 0 and j % number == 0 and i % number == 0:
                        badno += 1
                        break
    timeas = ((24 - h) * (60 * (60 - m))) - s
    goodno = timeas-badno
    # if h!=24:
    #     if m!=60:
    #         if s!=60:
    #
    print(badno,goodno)

while t>0:
    hh,mm,ss = map(int,input().split())

    #find prime from give second to 60
    for i in range(2,24):
        f=0
        for j in range(2 , i+1):
            if i!=j and i%j == 0:
                f=1
                break
        if f == 0:
            sslist.append(i)
    # print(len(sslist))
    t-=1
    check(hh,mm,ss,sslist)

