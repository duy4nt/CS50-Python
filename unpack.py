def total(galleons, sickles, knuts):
    return(galleons* 17+ sickles)* 29+ knuts

coins = [100, 50, 25]

print(total(*coins), "Knutss")
print(total(galleons= 200, sickles= 100, knuts= 50), "Knutss")