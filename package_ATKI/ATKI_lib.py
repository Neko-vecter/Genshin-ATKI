# Powered By Neko.vecter

class ATKI_lib():
    def __init__(self) -> None:
        super().__init__()
        self.ATK = 0 # Base ATK
        self.CTR = 0 # Crit RATE (In percentage)
        self.CTD = 0 # Crit DAM (In percentage)
        self.BNS = 0 # Bonus (like Cryo bonus)

    # 理想伤害=面板总攻击力*技能倍率*（1+物理/元素伤害加成百分比）*（1+暴击伤害百分比 * 暴击率）
    # Calculate Ideal Damage
    def cal_ATKI(self):
        print("Calculate ATKI")
        ATK_p = self.ATK 
        CTR_p = self.CTR / 100
        CTD_p = self.CTD / 100
        BNS_p = self.BNS / 100

        ID = ATK_p * (1+BNS_p) * (1+CTD_p * CTR_p)

        return ID

    # set var
    def set_ATK(self, ATK_i):
        self.ATK = ATK_i
        print("set ATK to", self.ATK)

    def set_CTR(self, CTR_i):
        self.CTR = CTR_i
        print("set CTR to", self.CTR)

    def set_CTD(self, CTD_i):
        self.CTD = CTD_i
        print("set CTD to", self.CTD)

    def set_BNS(self, BNS_i):
        self.BNS = BNS_i
        print("set Bonus to", self.BNS)
