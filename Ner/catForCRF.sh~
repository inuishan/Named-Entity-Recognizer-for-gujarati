cd ../New2
filename=($(ls))
cd ../Ner
for((i=0;i<${#filename[@]};i++))
do
python tagProper.py /home/sarafnikit/Guj/New2/${filename[i]} /home/sarafnikit/Guj/New3/${filename[i]}
echo tag
done
for((i=0;i<${#filename[@]};i++))
do
python prepareForCRF1.py /home/sarafnikit/Guj/New3/${filename[i]} /home/sarafnikit/Guj/New2/${filename[i]} /home/sarafnikit/Guj/New4/${filename[i]}
echo pre
done
for((i=0;i<${#filename[@]};i++))
do
cat /home/sarafnikit/Guj/New4/${filename[i]} | ./chunking1.py > /home/sarafnikit/Guj/New5/${filename[i]}
echo ca
done
