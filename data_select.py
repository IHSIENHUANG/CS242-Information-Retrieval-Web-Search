# read a parameter to select the file from cassandra
from cassandra.cluster import Cluster
import sys
#!/usr/bin/python
# -*- coding: UTF-8 -*-

cluster = Cluster()
session = cluster.connect()
rows = session.execute("SELECT cluster_name, listen_address FROM system.local")
for row in rows:
    session.execute("use info") 
    #datas= session.execute("SELECT * FROM data")
if len(sys.argv) <2:
    print ("Please input the file we want to select")
else:
    #num = sys.argv[1]
    #data_list = [eval(num)]
    data_list = [sys.argv[1]]
    data= session.execute("SELECT * FROM stem_index WHERE word= %s",data_list)
    for row in data:
        print("whole data {}").format(row)
        DF = row[1].split(";")
        #print (DF)
        for df in DF:
            #print (df)
            df = df.split(":")
            #print ("doc ID:  {}").format( df[0])
            if len(df[0]) >=1:
                data_list = [eval(df[0])]#take the doc id to select from database
                doc_datas = session.execute("SELECT doc_id,context,followers_c,location,time FROM data WHERE doc_id= %s",data_list)
                for doc_data in doc_datas:
                    print ("DATA:")
                    print (doc_data[0])#id
                    print (doc_data[1])#context
                    print (doc_data[2])#follower_c
                    print (doc_data[3])#locatino
                    print (doc_data[4])#time
        D_POS = row[2].split(";")
        TOTAL = row[3]       

