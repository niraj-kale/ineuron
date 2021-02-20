

l1 = [c*i for i in 'xyz' for c in range(1,5)]
print(l1)

l2 = [c*i for i in range(1,5) for c in 'xyz']
print(l2)

l31 = [[a+i] for a in range(2,5) for i in range(0,3)]
l32 = [[b+j for b in range(2,6)] for j in range(0,2)]
print(l31,l32)

l4 = [[a+i for a in range(4,8)] for i in range(0,2)]
print(l4)

l5 = [(a,b) for b in range(1,4) for a in range(1,4)]
print(l5)