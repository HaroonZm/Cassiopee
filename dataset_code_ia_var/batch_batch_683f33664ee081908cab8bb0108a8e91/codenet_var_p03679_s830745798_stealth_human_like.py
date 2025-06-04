# Bon, on va lire les entrées, je fais comme ça :
X, A, B = map(int, input().strip().split())

# je crois que c'est logique comme condition
if B <= A:
    print("delicious")
else:
    # alors là c'est peut-être pas super clair... mais je pense que ça marche
    if (B - A) > X:
        print("dangerous")
    else:
        print("safe")  # c'est ok dans ce cas je crois