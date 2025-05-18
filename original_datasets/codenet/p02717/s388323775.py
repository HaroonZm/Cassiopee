XYZ = input().split()
XYZ[0],XYZ[1],XYZ[2] = XYZ[2],XYZ[0],XYZ[1]
print(' '.join(map(str, XYZ)))