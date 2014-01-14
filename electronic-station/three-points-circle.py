from math import cos
import re

# Distance between points A and B
def distance(A,B):
    n = len(A)
    assert len(B) == n
    return sum((A[i]-B[i])**2 for i in range(0, n))**0.5

# Cosine of angle ABC
def cosine(A,B,C):
    a,b,c = distance(B,C), distance(A,C), distance(A,B)
    return (a*a+c*c-b*b)/(2*a*c)

# Cartesian coordinates of the point whose barycentric coordinates
# with respect to the triangle ABC are [p,q,r]
def barycentric(A,B,C,p,q,r):
    n = len(A)
    assert len(B) == len(C) == n
    s = p+q+r
    p, q, r = p/s, q/s, r/s
    return tuple([p*A[i]+q*B[i]+r*C[i] for i in range(0, n)])

# Cartesian coordinates of the point whose trilinear coordinates
# with respect to the triangle ABC are [alpha,beta,gamma]
def trilinear(A,B,C,alpha,beta,gamma):
    a = distance(B,C)
    b = distance(A,C)
    c = distance(A,B)
    return barycentric(A,B,C,a*alpha,b*beta,c*gamma)
               
# Cartesian coordinates of the circumcenter of triangle ABC
def circumcenter(A,B,C):
    cosA = cosine(C,A,B)
    cosB = cosine(A,B,C)
    cosC = cosine(B,C,A)
    return trilinear(A,B,C,cosA,cosB,cosC)

def checkio(data):
    points = []
    for match in re.finditer("\\(([0-9]+),([0-9]+)\\)", data):
        points.append([int(match.group(1)), int(match.group(2))])

    center = circumcenter(points[0], points[1], points[2])
    d = round(distance(center, points[0]), 2)

    center = [round(center[0], 2), round(center[1], 2)]
    center = [re.sub("\\.?0+$", "", str(center[0])), re.sub("\\.?0+$", "", str(center[1]))]
    d = re.sub("\\.?0+$", "", str(d))
    
    return "(x-{})^2+(y-{})^2={}^2".format(center[0], center[1], d)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

