import re,httplib2,bs4,os
URI=input("URI:")
data=httplib2.Http().request(URI)[1].decode("cp932")
print("data  .. OK")
tree=bs4.BeautifulSoup(data)
atags=tree.findAll("a")
uris=[]
for atag in atags:
	if atag["href"]:
		if re.search("\.(jpe?g|gif|png)",atag["href"]):
			uris.append(re.sub("/ime\.nu","",atag["href"]))
print(uris)
if uris:
	dirname="X" + str(hash(URI))
	os.mkdir(dirname)
for uri in uris:
	head,data=httplib2.Http().request(uri)
	if head["status"] != "200":
		print("[*]Passed %s" % uri)
		continue
	f=open("%s/X%s.jpg" % (dirname,str(hash(uri))),"wb")
	f.write(data)
	f.close()
	print("%s has been downloaded" % uri)
