name = 'Tore'

def hi(name):
	if name == "Henrietta":
		print ("du er kul azz")

	if name != "Henrietta":
		print ("skulle ønske du var Henrietta")

#hi('Henrietta')

def numbers():
	liste = (12345)
	for i in range (1,7):
		print(i)

	print (" ")

	tall = len(str(liste))
	for i in range (0, tall):
		print (i)

#numbers()

def lottery():
	lotnum= [3,64,9,100,78,93]
	lengde= len(lotnum)
	print (lengde)
	lotnum.sort()
	print(lotnum)
	print(lotnum[0])
	print(lotnum[4])

#lottery()

def dictionary():
	deltager = {"name" : "Henrietta", "land": "Norge"}
	print(deltager['name'])
	deltager['alder'] = '22'

	print(deltager['alder'])
	print(len(deltager))

dictionary()