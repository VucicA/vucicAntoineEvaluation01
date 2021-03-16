# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
    return "bonjour {}, comment allez-vous ?".format(msg)


###### exercice 01
def makeDico_T3(nomFichier, sep):
  fichier = open(nomFichier, 'r')
  dictionnaire = {}
  lignes = fichier.readlines()
  for ligne in lignes:
    x = ligne.split(sep)
    dictionnaire[x[0]] = x[1]
  print("Creation d'un dictionnaire a partir du fichier '{}' avec '{}' entrees".format(nomFichier, sep))
  return dictionnaire

###### exercice 02
def verifUrl_J2(url):
  result = url.split('.')
  if len(result) > 2:
    print("Url mal formee, trop  de '.'")
    print("test de '{}' : resultat = False".format(url))
    boolean = False   
  elif len(result[1]) > 3:
    print("Suffixe trop long")
    print("test de '{}' : resultat = False".format(url))
    boolean = False   
  else :
    print("test de '{}' : resultat = True".format(url))
    boolean = True  
  return boolean

###### exercice 03
def getTLD_P1(url):
  if(verifUrl_J2 == True):
    result = verifUrl_J2.split('.')
    if(result[1] == 'fr'):
      print("test de '{}' : resultat = True".format(url))
    else:
      print("test de '{}' : resultat = False".format(url))
      print("TLD mal forme")
  else:
    print("test de '{}' : resultat = False".format(url))
    print("TLD mal forme")

###### exercice 04
def VerifTLD_N3(tldOk, tld):
  for tldList in tldOk:
    if tld == tldList:
      print("test de '{}' : resultat = True".format(tld))
      boolean = True
    else:
      print("test de '{}' : resultat = False".format(tld))
      boolean = False
    return boolean

###### exercice 05
def ipVerifFormat_E1(adressIp):
  result = adressIp.split('.')
  if len(result) == 4:
    for resultChamp in result:
      if int(resultChamp) > 0 & int(resultChamp) < 256:
        print("test de '{}' : resultat = True".format(adressIp))
        boolean = True
        break
      else:
        print("test de '{}' : resultat = False".format(adressIp))
        boolean = False
  else:
    print("test de '{}' : resultat = False".format(adressIp))
    boolean = False
  return boolean

###### exercice 06
def makeTLD_Q7(dico):
  dico = makeDico_T3
  lignes = dico.split(',')
  for ligne in lignes:
    partie = ligne.split(':')
    

# Zone 2 ## zone pour les classes
###### exercice 07


###### exercice 08


###### exercice 09
    

# Zone 3 ## zone pour les tests des fonctions

def main() :
  from re import split
  ###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
  print("exercice 00 #######################")
  salutations = exempleHello("Michel")
  print(salutations)
  print(salutations.split(sep=" "))

	###### exercice 01
  print("exercice 01 #######################")
  dico = makeDico_T3("dns.txt", ",")
  print (dico)

	###### exercice 02
  print("exercice 02 #######################")
  verifUrl_J2('toto.fr')
  verifUrl_J2('to.to.fr')

	###### exercice 03
  print("exercice 03 #######################")
  getTLD_P1("toto.frog")

	###### exercice 04
  print("exercice 04 #######################")
  VerifTLD_N3(['fr', 'com', 'net'], 'fr')
  VerifTLD_N3(['fr', 'com', 'net'], 'fr')

	###### exercice 05
  print("exercice 05 #######################")
  ipVerifFormat_E1('1.1.1.1')
  ipVerifFormat_E1('1.1.1')

	###### exercice 06
  print("exercice 06 #######################")



	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")


	###### exercice 08
  print("exercice 08 #######################")


	###### exercice 09
  print("exercice 09 #######################")
	
	###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
  print("main()")
  main()