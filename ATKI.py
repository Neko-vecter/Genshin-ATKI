# Powered By Neko.vecter

from package_ATKI.ATKI_lib import ATKI_lib

atki = ATKI_lib()

atki.set_ATK(float(input("ATK \n")))
atki.set_CTR(float(input("CTR \n")))
atki.set_CTD(float(input("CTD \n")))
atki.set_BNS(float(input("BNS \n")))

print(atki.cal_ATKI())
