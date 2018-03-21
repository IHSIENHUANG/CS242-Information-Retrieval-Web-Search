# CS242-Information-Retrieval-Web-Search
## PURPOSE: Implement the Search Engineer
+ database come from twitter
+ Crawl Twitter with tweepy and twitter4j
+ Utilize Hadoop to do map reduce
+ Utilize lucene to create index
+ Compare the performance fo Hadoop and Lucene
+ NOSQL cassandra(cqlsh) to build the database
 
 ## FIIL INTRODUCTION
+ data_build.py : build data database
+ data_select.py: search the parameter from inverted index and get the docID and then go to search the database to get the context
+ index_build.py: build inverted index database
+ HTML and PHP for web

## DATABASE： Cassandra
### Introduction of Casaandra
+ key-value structure: time complexity O(1) on searching
+ Muiltiple Data Centers
+ It is not decided for really huge data
### What I Store
+ data : stroe the original data from json
+ map_reduce: store the inverted_index after map reduce
+ stem_index: store the data, proecessed by stem
+ location: map reduce processing on location

## Comparison of Lucene and Hadoop 
+ performance: Lucene is much betther than Hadoop
+ However, Hadoop is much harder to modify part of inverted index
