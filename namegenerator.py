import random

## function is here
def pickname():
    AD = ["Alexander", "Michael", "Onur", "Abuzer"]
    SOYAD =["Bell", "Faraday", "Y�ksel", "Sap"]
    adstr = random.choice(AD)
    soyadstr = random.choice(SOYAD)

    return "{} {}".format(adstr, soyadstr)

######################
## Main Program Here
######################

for i in range (5):
    name = pickname()
    if name == "Onur Y�ksel":
        print(name)
    else:
        print("Not Found")
