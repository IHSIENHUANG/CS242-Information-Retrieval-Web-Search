# CS242-Information-Retrieval-Web-Search
## PURPOSE: Implement the Search Engineer
+ database come from twitter
+ Crawl Twitter with tweepy and twitter4j
+ Utilize Hadoop to do map reduce
+ Utilize lucene to create index
+ Compare the performance fo Hadoop and Lucene
+ NOSQL cassandra(cqlsh) to build the database
+ build web UI with js

## FILE INTRODUCTION:
+ data_build.py : build data database
+ data_select.py: search the parameter from inverted index and get the docID and then go to search the database to get the context
+ index_build.py: build inverted index database
