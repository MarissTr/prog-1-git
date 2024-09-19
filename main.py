class Mašīnas:
    def __init__(self,modelis,krasa,marka):
        self.modelis = modelis
        self.marka = marka
        self.krasa = krasa
    def est(self):
        print("sveiki")

m1= Mašīnas("BMW","E90","melns")
m1.est()