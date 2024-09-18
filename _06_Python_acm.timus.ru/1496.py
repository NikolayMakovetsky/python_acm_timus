"""Given"""
sm = "@@@ ttt mmm mmm @@@ @@@ asdf dfg ttt    234j   kjf      loortbbn ttt dfd kfjfd    @@@"
sm_list = sm.split()
sm_set = set(sm.split())

k = 0
for i in sm_set:
    for j in sm_list:
        if i == j:
            k += 1
    if k > 1:
        print(i)
    k = 0
