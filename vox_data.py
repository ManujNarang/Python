
import urllib
import string
from BeautifulSoup import *

#initializing the department dictionaries to stande data 

current = dict()
ae_dept= dict()
ee_dept= dict()
cse_dept= dict()
mse_dept= dict()
bsbe_dept= dict()
me_dept= dict()
ce_dept= dict()
che_dept= dict()
mth_dept= dict()
chm_dept= dict()
eco_dept= dict()
phy_dept= dict()
others=dict()

#checking fand Y14 data

for i in range(1,819):

	if (i<10):
		url = 'http://172.26.142.68/examscheduler2/personal_schedule.php?rollno=1300'+str(i)
	elif(i<100):
		url = 'http://172.26.142.68/examscheduler2/personal_schedule.php?rollno=130'+str(i)
	else :
		url = 'http://172.26.142.68/examscheduler2/personal_schedule.php?rollno=13'+str(i)
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('td')
	cnt=0
	for tag in tags:
			if(str(tag.contents[0])[0]=='<')or (str(tag.contents[0])=='Not Sch / LAB'):
				cnt=cnt+1
			elif not(str(tag.contents[0])[0].isdigit()):	
				current[str(tag.contents[0])]= current.get(str(tag.contents[0]),0)+1
	
	
	if ('MTH424A' in current) and ('MTH308A' in current) : 	
		for tag in current:
			for key in current:
				mth_dept[key]=mth_dept.get(key,0)+1
			break
	elif('AE341A' in current) and ('AE351A' in current)and('AE361A' in current) : 	
		for tag in current:
			for key in current:
				ae_dept[key]=ae_dept.get(key,0)+1
			break
	elif('MSE304A' in current) and  ('MSE305A' in current)and('MSE312A' in current)and('MSE314A' in current)and('MSE315A' in current) : 	
		for tag in current:
			for key in current:
				mse_dept[key]=mse_dept.get(key,0)+1
			break
	elif('CHE331A' in current) and ('CHE381A' in current)and('CHE391A' in current) : 	
		for tag in current:
			for key in current:
				che_dept[key]=che_dept.get(key,0)+1
			break
	elif('EE340A' in current) and  ('EE381A' in current) : 	
		for tag in current:
			for key in current:
				ee_dept[key]=ee_dept.get(key,0)+1
			break
	elif('CS335A' in current) : 	
		for tag in current:
			for key in current:
				cse_dept[key]=cse_dept.get(key,0)+1
			break
	elif('BSE321A' in current) and ('BSE322A' in current): 	
		for tag in current:
			for key in current:
				bsbe_dept[key]=bsbe_dept.get(key,0)+1
			break
	elif('ME341A' in current)and ('ME351A' in current)and('ME354A' in current) : 	
		for tag in current:
			for key in current:
				me_dept[key]=me_dept.get(key,0)+1
			break
	elif('CE352A' in current)and ('CE382A' in current)and ('CE372A' in current) : 	
		for tag in current:
			for key in current:
				ce_dept[key]=ce_dept.get(key,0)+1
			break
	elif('CHM342A' in current)and ('CHM322A' in current)and('CHM344A' in current) : 	
		for tag in current:
			for key in current:
				chm_dept[key]=chm_dept.get(key,0)+1
			break
	elif('ECO311A' in current)and ('ECO342A' in current): 	
		for tag in current:
			for key in current:
				eco_dept[key]=eco_dept.get(key,0)+1
			break
	elif('PHY412A' in current)and ('PHY473A' in current)and('PHY399A' in current) : 	
		for tag in current:
			for key in current:
				phy_dept[key]=phy_dept.get(key,0)+1
			break
	else:	
		for tag in current:
			for key in current:
				others[key]=others.get(key,0)+1
			break
	
	current.clear()
print "mathematics"
print mth_dept
print "aero"
print ae_dept
print "elec"
print ee_dept
print "cse"
print cse_dept
print "mse"
print mse_dept
print "bsbe"
print bsbe_dept
print "me"
print me_dept
print "ce"
print ce_dept
print "che"
print che_dept
print "chm"
print chm_dept
print "eco"
print eco_dept
print "phy"
print phy_dept
print "others"
print others



	



    
