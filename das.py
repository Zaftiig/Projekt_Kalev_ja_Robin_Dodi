def kooslubajad(järjend):
    sarnasus = 0
    ennik = (0, 0)
    
    for i in range(len(järjend)):
        for j in range(i+1,(len(järjend))):
            if len(järjend[i] & järjend[j]) > sarnasus:
                sarnasus = len(järjend[i] & järjend[j])
                a = i
                b = j

    return (a, b)
kooslubajad([{"algatada koduloometoetus", "kuritegevust vähendada", "kõiki toetusi suurendada", "kaotada kõik maksud", "suurendada kõigi palkasid", "rajada spordiväljakud igasse linna"},
                 {"toetada pensionäre", "aidata noorperesid", "edendada maaelu", "suurendada vastsündinute arvu", "vähendada suremust"}])