sez=[12, 5, 8, 21, 3, 16, 9, 14]

def vsota_stevil(sez):
    vsota = 0
    for i in range(len(sez)):
        vsota+= sez[i]
    print(vsota)

#vsota_stevil(sez)

def povp_vred(sez):
    vsota = 0
    for i in range(len(sez)):
        vsota+= sez[i]
    print(vsota / len(sez))

#povp_vred(sez)

def najvecje_st(sez):
    max_st = sez[0]
    for i in range(1,len(sez)):
        if sez[i] > max_st:
            max_st = sez[i]
    print(max_st)

#najvecje_st(sez)

def najmanjse_st(sez):
    min_st = sez[0]
    for i in range(1,len(sez)):
        if sez[i] < min_st:
            min_st = sez[i]
    print(min_st)

#najmanjse_st(sez)

def prestej_sodo(sez):
    stevec=0
    for i in range(len(sez)):
        if sez[i] % 2 == 0:
            stevec+=1
    print(stevec)

prestej_sodo(sez)