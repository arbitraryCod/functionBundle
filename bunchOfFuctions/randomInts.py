import random
def subMenue():
    running=True
    while running:
        inp=int(input("random max :"))
        if inp>=0 and inp<=1000:
            z=[random.randint(1,inp)for i in range(20)]
            print(z)
            print(min(z))
            print(max(z))
            print(sum(z)/20)
            inp=input("run again(y/n) : ")
            if inp=="n":
                running=False
