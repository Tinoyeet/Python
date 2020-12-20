__author__ = "Tino"

print("Wie heißt du?")
name = input()
print("Du heißt " + name + " Wenn ja dann schreib ja!")
yene = input()
if yene == "Ja":
    print("Ok du heißt also " + name + " hab einen schönen Tag!")
    input("Enter um zu beenden!")
elif yene == "ja":
    print("Ok du heißt also " + name + " hab einen schönen Tag!")
    input("IEnter um zu beenden!")
elif yene == "Nein":
    while 3 > 2:
        print("Was ist dann dein Name")
elif yene == "nein":
    while 3 > 2:
        print("Was ist dann dein Name")
else:
    print("Ich weiß nicht was du meinst!")
    input("Enter um zu beenden!")