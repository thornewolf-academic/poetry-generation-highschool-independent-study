import urllib.request as req
import re
for sonnetIndex in range(130,155):
	reg=re.compile("<p id='sonnettext'>([^\d]+?)&")
	reg=re.compile("sonnettext(.+?)&")
	r=req.urlopen('http://www.shakespeares-sonnets.com/sonnet/{}'.format(sonnetIndex))
	r=str(r.read())
	#print(r)
	q=reg.findall(r)[0].strip("\\<>").replace('<em>','').replace('</em>','').replace('<br />','').replace("\\'",'').replace('>','').replace('\\r','').replace('\\n','\n').replace("'",'')
	with open('./Poems/Limerick/mySonn{}.txt'.format(sonnetIndex),'w') as f:
		f.write(q)