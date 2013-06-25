from sys import argv
import string
script, filename = argv

txt = open(filename) #opens file and saves to file descriptor txt


yelp_dict={}
# yelp_dict = {txt.replace("\n", ",")}  THIS DID NOT WORK
# print txt
#take each line of scores and enter as key/value in dictionary
for line in txt:
	pairs = line.strip('\n').split(":")
	#print pairs 		#pairs is a list of key,value pairs
	yelp_dict[pairs[0]] = pairs[1]
	
for key, value in sorted(yelp_dict.iteritems()):
	print "Restaurant %s is rated %s" % (key, value)

#print yelp_dict
	#takes in string,strips new lines, splits it to a list
	#for word in line.strip('\n').split():
		
	
#for key, value in yelp_dict.iteritems():
#	print "Restaurant %s is rated a %d" % (key, value)

