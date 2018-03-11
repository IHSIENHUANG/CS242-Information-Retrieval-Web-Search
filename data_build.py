# input parameter and get data from cassandra
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
rows = session.execute("SELECT cluster_name, listen_address FROM system.local")
for row in rows:
    print(row.cluster_name, row.listen_address)
    session.execute("use info") 
    datas= session.execute("SELECT * FROM data")
    for data in datas:
        print (data)
    #session.execute("INSERT INTO data(doc_id,name,context,location,followers_c)VALUES(0,'name','context','london',25)")
    #var0 = 10
    #var1 = "1"
    
    #session.execute("INSERT INTO data(doc_id,name)VALUES("+var0+",'"+var1+"')")
    #session.execute("INSERT INTO data(doc_id,name)VALUES(%s,%s)",(data_list))
with open('output.txt', 'r') as f: 
    data = f.readlines()
    var =0
    for line in data:
     
    	words = line.split("}")
        var = var +1
        
        print (var) 
            #data_list=[words[0],words[1],words[2],words[3],words[4]]
            #session.execute("INSERT INTO data(doc_id,name,context,location,followers_c)VALUES(%s,%s,%s,%s,%s)",(data_list))
        if len(words) !=5:
            print ("{} {} : length is not enough").format(var,len(words))
            data_list=[var,"NULL","NULL","NULL",0]
        else:
            data_list=[eval(words[0]),words[1],words[2],words[3],eval(words[4])]
        session.execute("INSERT INTO data(doc_id,name,context,location,followers_c)VALUES(%s,%s,%s,%s,%s)",data_list)

