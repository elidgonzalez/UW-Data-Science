register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- filter rdfabout.com
filtered_triples = FILTER ntriples BY subject matches '.*rdfabout\\.com.*';

-- copy filtered data
filtered_triples_2  = 
FOREACH filtered_triples GENERATE subject as subject2, predicate as predicate2, object as object2;

-- join
joined_triples = JOIN filtered_triples BY object, filtered_triples_2 BY subject2;

-- drop duplicates
joined_triples_distinct = DISTINCT joined_triples;

-- order by predicate
results = ORDER joined_triples_distinct BY predicate;

-- store the results in the folder /user/hadoop/example-results
store results into '/user/hadoop/problem3b-results' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_subject_ordered into 's3n://superman/example-results';
