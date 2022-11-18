mkdir helloWorld
cd helloWorld
echo "The command echo is like Linux's version of print()"
echo "But if we tell echo to put its output into a text file like below..."
echo "It shows up where we tell it to!" > helloWorld.txt
git add helloWorld.txt
git commit -m "Adding output of testScript.sh"
git push
