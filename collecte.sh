#!/usr/bin/env zsh

# Au préalable, je vous conseil de séparer vos séries en trois dossiers. Pour ce
# faire, allez dans le dossier qui contient tout le data et entrez les commandes
# suivantes:
#
# mkdir ../serie1 ../serie2 ../serie3
# cp $(ls | grep "testset_[0-9]\+_[0-9].txt") ../serie1
# cp $(ls | grep "testset_[0-9]\+_1[0-9].txt") ../serie2
# cp $(ls | grep "testset_[0-9]\+_2[0-9].txt") ../serie3
#
# Vous pouvez par après vous inspirer de ce script pour évaluer toutes les
# séries avec tous les algorithmes.

for algo in {"retourArriere","kek"}; do
    # Pour chaque fichier de série.
    for serie in {"poset10","poset14","poset18","poset22","poset26","poset30"}; do
        for taille in {"4","6","8","10"}; do
            # Pour chaque exemplaire dans une série.
            for ex in $(ls $serie/$taille); do
                # On receuille le temps d'exécution dans t.
                t=$(timeout 180 ./tp.sh -a $algo -e ${serie}/${taille}/${ex} -t -p)
                # Si jamais on mesure un temps, on l'insère dans le bon fichier.
                if [ t != "" ]; then
                    echo $t >> ./results/${algo}_${serie}_${taille}.csv
                fi
            done
        done
    done
done
