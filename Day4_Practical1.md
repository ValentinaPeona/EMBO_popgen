

```bash
for i in 3 4 5 6 7 8
do
 echo "K=" $i
 software/admixture_linux-1.22/admixture ./data/BrahuiYorubaSimulationChrom22.admixture.geno $i --c > BrahuiYorubaSimulationChrom22.admixture.$i.C
 echo "done K=" $i
done

```