import graphics.tdgraphics.cuboid as cb
import graphics.tdgraphics.sphere as sp
import graphics.rectangle as rectangle
import graphics.circle as cr

r=int(input("enter the radius"))
cr.carea(r)
cr.cperi(r)
l=int(input("enter the length of rectangle"))
b=int(input("enter the breadth of rectangle"))
h=int(input("enter the height of rectangle"))
rectangle.rarea(l,b)
rectangle.rperi(l,h)
s=int(input("enter the radius of sphere"))
sp.spr_circum(s)
sp.spr_area(s)
lc=int(input("enter the length of cuboid"))
wc=int(input("enter the breadth of cuboid"))
bc=int(input("enter the height of cuboid"))
cb.cubarea(lc,wc,bc)
cb.cubperi(lc,wc,bc)


rectangle.py:-

def rarea(l,b):
    r_area=l*b
    print("area of rectangle:",r_area)
def rperi(l,h):
    r_peri=2*(l+h)
    print("perimeter of rectangle:",r_peri)
    

circle.py:-


def carea(r):
    c_area=3.14*r*r
    print("area of circle:",c_area)
def cperi(r):
    c_peri=3.14*r*2
    print("perimeter of circle:",c_peri)


cuboid.py:-

def cubarea(l,b,h):
    cub_a=2*(l*b+b*h+b*l)
    print("area of cuboid",cub_a)

def cubperi(l,b,h):
    cub_p=4*(l+b+h)
    print("perimeter of cuboid",cub_p)
    

sphere:-

def spr_circum(r):
    c=2*3.14*r
    print("circumference of spere:",c)

def spr_area(r):
     a=4*3.14*r*r
     print("surface area of a spere:",a)



