def tri_area(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        s=(a+b+c)/2
        area=(s*((s-a)*(s-b)*(s-c)))**0.5
        print("Area of Triangle is",round(area,2))
    else:
        print("Triangle is not possible by the given values")
    return
a,b,c=float(input("a=?")),float(input("b=?")),float(input("c=?"))
tri_area(a,b,c)
    
    