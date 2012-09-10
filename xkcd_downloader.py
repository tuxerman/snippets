"""
downloads all XKCD strips and hover-captions within the numbers specified

This code is free to copy, modify, distribute, eat sleep or swear at. Just credit me somewhere.

Sriram Padmanabhan
screamingwdm2 at gmail dot com
"""

import re,urllib,os,subprocess

mainpage=urllib.urlopen("http://www.xkcd.org")
mainpage_html=mainpage.read()

latest_num=int(re.search(r'Permanent link to this comic: http://xkcd.com/(.*)/<br.*',mainpage_html).group(1))
print 'Latest comic number is',latest_num
rangeinput=raw_input('\nEnter comics to download (eg: "55,630,666-999,1024": ')

comiclist=list()

for (num_left,num_right,num_single) in re.findall(r'(\d+)-(\d+)|(\d+)',rangeinput):
	if num_single is not '':
		comiclist.append(int(num_single))
	if num_left is not '' and num_right is not '':
		for i in range(int(num_left),int(num_right)+1):
			comiclist.append(i)
#print comiclist

url_error=list()
wget_arg=''
fnull = open(os.devnull, 'w')
os.system('[ -d xkcd_downloaded ] || mkdir xkcd_downloaded')
fnull.close()

for comic in comiclist:
   	try:
		comic_url="http://xkcd.com/"+str(comic)
		print 'Opening ',comic_url,'...'
		page=urllib.urlopen(comic_url).read()
		img_url=re.search(r'Image URL \(for hotlinking/embedding\): (.*png)',page).group(1)
		img_name=re.search(r'/(\w*).png',img_url).group(1)
		comic_transcript=re.search(r'http://imgs.xkcd.com/comics/.*\.png" title="(.*)" alt',page).group(1)
		wget_arg+=img_url+' ' #add image url to wget list
	
	except AttributeError:	#most probably a regex that failed to match
		url_error.append(comic)
		continue
		
	#convert special characters in transcript
	comic_transcript=comic_transcript.replace("&#39;","'")
	comic_transcript=comic_transcript.replace("&amp;","&")
	comic_transcript=comic_transcript.replace("&quot;",'"')
	comic_transcript=comic_transcript.replace("&lt;","<")
	comic_transcript=comic_transcript.replace("&gt;",">")

	#save transcript
	ftext=open("./xkcd_downloaded/"+img_name+".txt",'w')
	ftext.write(comic_transcript)
	ftext.flush()
	
#run wget for all the links
os.system('cd xkcd_downloaded;wget -nv -nc '+wget_arg)

print 'Could not fetch comics numbered: ', url_error #todo FIXME
