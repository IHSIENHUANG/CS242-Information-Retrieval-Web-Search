# input parameter and get data from cassandra
from cassandra.cluster import Cluster
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
cluster = Cluster()
session = cluster.connect()
rows = session.execute("SELECT cluster_name, listen_address FROM system.local")
for row in rows:
    print(row.cluster_name, row.listen_address)
    session.execute("use info") 
    datas= session.execute("SELECT * FROM map_reduce")
    for data in datas:
        print (data)
    #session.execute("INSERT INTO data(doc_id,name,context,location,followers_c)VALUES(0,'name','context','london',25)")
    #var0 = 10
    #var1 = "1"
    
    #session.execute("INSERT INTO data(doc_id,name)VALUES("+var0+",'"+var1+"')")
    #session.execute("INSERT INTO data(doc_id,name)VALUES(%s,%s)",(data_list))
with open('part-r-00000', 'r') as f: 
    data = f.readlines()
    var =0
    for line in data:
     
    	
        words = line.split("\t")
        
        #print ("@@ {}").format( words[0])
        #print ("@@ {}").format( words[1])
        TF = words[1].split("DF:")
        TF[0]=TF[0].replace(";",'')
        #print ("@@ {}").format(TF[0][3:])
        DF = TF[1].split("I:") 
        #print ("@@ {}").format(DF[0])
        DF[1] = DF[1].replace("\n"," ")
        #print ("@@ {}").format(DF[1])

        var = var +1
        
        print (var) 
        data_list=[words[0],DF[0],DF[1],eval(TF[0][3:])]
        session.execute("INSERT INTO map_reduce(word,doc_f,doc_index,total)VALUES(%s,%s,%s,%s)",data_list)    
        
