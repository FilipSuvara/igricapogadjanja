import random
zamisljenBroj=random.randint(0,20)
brojPokusaja=5
while brojPokusaja>0:
    mojePogadjanje=int(input("pogadjaj: "))
    if mojePogadjanje==zamisljenBroj:
        print("BRAVO,IGRAJ LOTO")
        break
    else:
        print("NETACNO,AKO IMAS JOS ZIVOTA PROBAJ PONOVO")
        brojPokusaja=brojPokusaja-1
    if(brojPokusaja==0):
        print("kraj igre,probaj opet")
