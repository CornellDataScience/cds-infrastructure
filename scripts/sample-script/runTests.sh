python identifyTest.py
file="pytests.txt"
while read -r line; 
do 
  pytest "$line" >> pytest_out.txt; 
done < "$file"

git add pytest_out.txt
git commit -m "Output of run tests "
git push