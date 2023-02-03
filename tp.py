#pageRank implementation
#propagation d'épidemie
# on a 7115
# taille de matrice 7115²

def buildMatrix():
    #extreaire le fichier
    with open('Wiki-Vote.txt') as f:
        i = 1
        while i:
            line = f.readline()
            if not line:
                break
            link = line.strip()
            for node in link.split():
                print(node)
            i-=1


buildMatrix()
