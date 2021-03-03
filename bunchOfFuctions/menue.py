import functionArea
import randomInts
import unitConversion
running=True
while running:
    inp=int(input("area of shape (1) | random int(2) | unit conversion(3) | binary sums(4) |exit(5) : "))
    if inp==1:
        functionArea.subMenue()
    elif inp==2:
        randomInts.subMenue()
    elif inp==3:
        unitConversion.gigaConvert()
    elif inp==4:
        pass
    elif inp==5:
        running=False
