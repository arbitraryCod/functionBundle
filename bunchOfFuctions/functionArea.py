import math
def areaOfRect(l,w):
    return(l*w)
def areaOfCircle(r):
    return(r*r*math.pi)
def areaOfTriangle(b,h):
    return(b*h/2)
def areaOfcuboid(l,w,h):
    return ((2*l*w)+(2*l*h)+(2*w*h))
def areaOfSphere(r):
    return(4*r*r*math.pi)
def subMenue():
    running=True
    while running:
        inp=int(input("dimentions (2-3) : "))
        if inp==2:
            running2=True
            while running2:
                inp2=int(input(("area of rect (1) | area of circle (2) | area of triangle(3) : ")))
                if inp2==1:
                    print(areaOfRect(int(input("length : ")),int(input("width"))))
                    running2=False
                if inp2==2:
                    print(areaOfCircle(int(input("radius : "))))
                    running2=False
                if inp2==3:
                    print(areaOfTriangle(int(input("base : ")),int(input("hieght"))))
                    running2=False
        if inp==3:
            running2=True
            while running2:
                inp2=int(input(("area of cuboid (1) | area of sphere (2) : ")))
                if inp2==1:
                    print(areaOfCuboid(int(input("length : ")),int(input("width")),int(input("hieght : "))))
                    running2=False
                if inp2==2:
                    print(areaOfSphere(int(input("radius : "))))
                    running2=False
        inp=input("run again (y/n) : ")
        if inp=="n":
            running=False
