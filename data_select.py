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
    data= session.execute("SELECT * FROM map_reduce WHERE word= %s",data_list)
    for row in data:
        DF = row[1].split(";")
        #print (DF)
        for df in DF:
            #print (df)
            df = df.split(":")
            print ("doc ID:  {}").format( df[0])
            if len(df[0]) >=1:
                data_list = [eval(df[0])]
                doc_datas = session.execute("SELECT context FROM data WHERE doc_id= %s",data_list)
                for doc_data in doc_datas:
                    print (doc_data)
        D_POS = row[2].split(";")
        TOTAL = row[3]       

