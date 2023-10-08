cuvinte_romana = ['mama', 'tata']
cuvinte_engleza = ['mother', 'father']


while True:
    cheie = input("1 pentru romana, 2 pentru eng: ")

    while cheie != '1' and cheie != '2':
        cheie = input("baga iar 1 sau 2: ")

    if cheie == '1':
        cuvant = input("baga cuvant in romana: ")
        if cuvant in cuvinte_romana:
            index = cuvinte_romana.index(cuvant)
            print(cuvinte_engleza[index])
        else:
            raspuns = input("nu il avem in baza de date. Stii traducerea(yes/no):")
            if raspuns == 'yes':
                traducere = input('baga traducere: ')
                cuvinte_romana.append(cuvant)
                cuvinte_engleza.append(traducere)
            else:
                print('nu exista traducere')

    else:

            word = input("enter the word: ")
            if word in cuvinte_engleza:
                index = cuvinte_engleza.index(word)
                print(cuvinte_romana[index])
            else:
                answer = input("nu il avem in baza de date. Stii traducerea(yes/no):")
                if answer == 'yes':
                    translate = input('baga traducere: ')
                    cuvinte_romana.append(translate)
                    cuvinte_engleza.append(word)
                else:
                    print('nu exista traducere')

