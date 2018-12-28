"""
Author: @abhigyan
"""

from bs4 import BeautifulSoup

with open('sample.html') as webpage:
		soup = BeautifulSoup(webpage, 'lxml')

# Looping through the elements. Each idx tag contains data for each word of the dictionary

for idx in soup.find_all('idx:entry'):
	for l in idx.find_all('idx:orth'):
		print(l['value']) # Word

	temp = []
	for a in idx.find_all('idx:iform'): #Related words
		try:
			temp.append(str(a['value']))
		except:
			pass
	if len(temp)>0:
		print("Related: " + str(" ".join(temp)))
	else:
		pass

	for a in idx.find_all('a'): # Part_of_speech
		try:
			main_pos = a.find('font', color="green").text
			print("Primary PartOfSpeech: " + str(main_pos))
		except:
			pass
	for a in idx.find('a'): # Part_of_speech
		try:
			main_pos = idx.find('font', color="green").text
			print("Primary PartOfSpeech: " + str(main_pos))
		except:
			pass

	f = idx.a.next_siblings # Meaning
	for i in f:
		try:
			for j in i.find_all('div', width="9"):
				if str(j.b) == "<b>1</b>":
					print("Meaning: " + str(j.text))
				else:
					pass
		except:
			pass


	f = idx.a.next_siblings
	for i in f:
		try:
			for j in i.find_all('font'):

				if j['color'] =="chocolate": # Secondary part of speech
					print("Other PartOfSpeech: " + str(j.b.text))
				else:
					pass

				if j['color'] =="#595959": # Usage
					print("usage:" + str(j.text))
				else:
					pass

				if j['color'] =="darkslateblue": # Secondary Meaning
					print("Synonyms: " + str(j.b.text))
				else:
					pass
		except:
			pass
	print('\n')