cd ../New2
filename=($(ls))
cd ../Ner
for((i=0;i<${#filename[@]};i++))
do
tail -n +3 /home/sarafnikit/Guj/New4/${filename[i]} | ./chunking1.py > /home/sarafnikit/Guj/New5/${filename[i]}
echo ca
done
