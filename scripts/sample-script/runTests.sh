python identifyTest.py

dt=`date '+%d_%m_%Y_%H:%M:%S'`
file="pytests.txt"
fileout="pytest_out_$dt.txt"

while read -r line; 
do 
  pytest "$line" >> "$fileout";
done < "$file"

rm "$file"
git add "$fileout"
git commit -m "Output of run tests "
git push