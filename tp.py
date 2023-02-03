# pageRank implementation
# propagation d'épidemie
# on a 7115
# taille de matrice 7115²

def buildMatrix():
    # init array
    rows, cols = (7115, 7115)
    transition_mtx = [[0]*cols]*rows
    #créer un dict pour faire les liens
    dict_link = {}
    temp = []
    #for row in transition_mtx:
    #print(row)
    
    # extreaire le fichier
    with open('Wiki-Vote.txt') as f:
        i = 1
        while i:
            line = f.readline()
            if not line:
                break
            link = line.strip()
            for node in link.split():
                temp.append(node)
                dict_link[temp[0]] = temp[1]
            i -= 1
            print(temp[1])


buildMatrix()
