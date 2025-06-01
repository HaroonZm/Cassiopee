import sys, math, os

def main():
    RADIUS_EARTH = 6378.1
    PI_DIV_180 = math.pi / 180
    ENV_CHECK = os.getenv('PYDEV', '') == 'True'

    if ENV_CHECK:
        sys.stdin = open("sample-input.txt", "r")

    def to_radians(deg):
        # Personnalisation: fonction utilitaire intérieure avec annotation de type bizarre (float in float out)
        return deg * PI_DIV_180

    while 1 == 1:
        line = sys.stdin.readline()
        if not line:
            break  # élégance non conventionnelle : utiliser readline + break

        parts = line.split()
        # vérification non-conventionnelle
        if parts == ['-1', '-1', '-1', '-1']:
            break

        l1, g1, l2, g2 = map(lambda x: to_radians(float(x)), parts)

        # Formule avec décomposition étrange dans variables intermédiaires
        s1 = math.sin(l1)
        s2 = math.sin(l2)
        c1 = math.cos(l1)
        c2 = math.cos(l2)
        diff_long = g2 - g1
        cc = math.cos(diff_long)
        
        inner = s1 * s2 + c1 * c2 * cc

        # Forcer dans [-1,1] pour éviter erreurs float peu communes (idiosyncrasie du dev)
        if inner > 1.0:
            inner = 1.0
        elif inner < -1.0:
            inner = -1.0

        distance = RADIUS_EARTH * math.acos(inner)
        print(int(round(distance, 0)))

if __name__ == '__main__':
    main()