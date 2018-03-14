# read a parameter to select the file from cassandra
from cassandra.cluster import Cluster
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
input_data =sys.argv[1].split(" ")
for test in input_data:
    data_list = [test.lower()]#all of the word in database will transform to lower case

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
                score = 0
                datas = session.execute("SELECT doc_id ,followers_c FROM data WHERE doc_id= %s",data_list)
                #num = datas[0] 
		for num in datas:

		    #print num[0]
		    #print num[1]
                    score =num[1]
		    break
			

		#if datas[0] != None or int(datas[1]) != 0:
		#    print datas[1]
               # else:
		#    score = 0
	      
                if df[0] in output.keys():
                    output[df[0]]  += int(score)#
                else:
                    output[df[0]] = int(score)#df[0] docid df[1]:frequency
                '''
                doc_datas = session.execute("SELECT doc_id,context,followers_c,location,time FROM data WHERE doc_id= %s",data_list)
                for doc_data in doc_datas:
                    print ("DATA and frequency ", word_frequency_doc)
                    print (doc_data[0])#id
                    print (doc_data[1])#context
                    print (doc_data[2])#follower_c
                    print (doc_data[3])#locatino
                    print (doc_data[4])#time
        D_POS = row[2].split(";")
        TOTAL = row[3]       
    ''' 
sorted_output = sorted(output.items(), key = operator.itemgetter(1) , reverse = True)
rou = 0 
for out in sorted_output:
    #rou += 1
    #if rou >=10:
     #   exit()
    data_list = [int(out[0])]
    doc_datas = session.execute("SELECT name,context,followers_c,location,time FROM data WHERE doc_id= %s",data_list)
    for doc_data in doc_datas:
        print ("DATA and score ",out[1])
        print (doc_data[0])#id
	str = doc_data[1]
	print str.encode("utf-8")
        #print (doc_data[1])#context
        print (doc_data[2])#follower_c
	str2 = doc_data[3]
	print str2.encode("utf-8")
        #print (doc_data[3])#locatino
        print (doc_data[4])#time
