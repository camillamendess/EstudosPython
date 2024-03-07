medida = (float(input("Uma ditância em metros")))
print('A medida de {}m corresponde a {:.0f}mm, {:.0f}cm, {:.0f}dm, {:.0f}dam, {:.0f}hm, {:.0f}km'.format(medida,(medida*1000),(medida*100), (medida*10), (medida/10),(medida/100),(medida/1000)))
