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

povp_vred(sez)