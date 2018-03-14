# read a parameter to select the file from cassandra
from cassandra.cluster import Cluster
from numpy import arange
import sys
import math
import operator
#!/usr/bin/python
# -*- coding: UTF-8 -*-

TOTAL_DOC = 1229366
k1= 1.2
b=0.7
k2=100
K = 1


cluster = Cluster()
session = cluster.connect()
rows = session.execute("SELECT cluster_name, listen_address FROM system.local")
for row in rows:
    session.execute("use info") 
    #datas= session.execute("SELECT * FROM data")
if len(sys.argv) <2:
    print ("Please input the file we want to select")
#print len(sys.argv)
output = {}
input_data = [sys.argv[0]]
input_data =sys.argv[1].split(" ")
'''
for test in input_data:
    print (test)
    print (len(input_data))
'''
for test in input_data:
    #data_list = [input_data[i].lower()]#all of the word in database will transform to lower case
    data_list = [test.lower()]
    #print (data_list)
    
    data= session.execute("SELECT * FROM stem_index WHERE word= %s",data_list)
    for row in data:
        #print("whole data {}").format(row)
        #print("pos: {}").format(row[2])
        DF = row[1].split(";")

        QUERY_DOC_NUM = len(DF)#this query in how many nums of docs

        for df in DF:
            #print (df)
            df = df.split(":")
            #print ("doc ID:  {}").format( df[0])
            if len(df[0]) >=1:
                data_list = [eval(df[0])]#take the doc id to select from database
                if len(df[1]) <1:
                    df[1] =0
                word_frequency_doc = [eval(df[1])]
                score = math.log(1.0/((QUERY_DOC_NUM+0.5)/(TOTAL_DOC-QUERY_DOC_NUM+0.5)))*((k1+1)*int(df[1])/(K+int(df[1])))*((k2+1)/(k2))
                if df[0] in output.keys():
                    #output[df[0]]  = eval(output[df[0]]+df[1])#
                    output[df[0]]  += int(score)#
                else:
                    output[df[0]] = int(score)#df[0] docid df[1]:frequency
sorted_output = sorted(output.items(), key = operator.itemgetter(1) , reverse = True)
rou =0
for out in sorted_output:
    #rou +=1
    #if rou >=10:
    #    exit()    
    data_list = [int(out[0])] 
    doc_datas = session.execute("SELECT name,context,followers_c,location,time FROM data WHERE doc_id= %s",data_list)
  
    
    
    for doc_data in doc_datas:
        print ("DATA and score ",out[1])
	str = doc_data[1]
        print (doc_data[0])#id
	str = doc_data[1]
	print str.encode("utf-8")
        #print str.encode("utf-8")
	#print (doc_data[1])
	print (doc_data[2])#follower_c
	str2 = doc_data[3]
	print str2.encode("utf-8")
        #print (doc_data[3])#locatino
        print (doc_data[4])#time
    #print ("hello1")
    #print ("hello2")
    #print "hello3"
    #print "hello4"
    #print "hello5"
    #print "hello6"

