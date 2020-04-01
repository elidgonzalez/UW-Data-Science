SELECT A.docid, B.docid, sum(A.count * B.count) s
FROM (SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) AS A, (SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) AS B 
WHERE A.term = B.term AND A.docid < B.docid 
AND (A.docid = 'q' OR B.docid = 'q')
GROUP BY A.docid, B.docid 
ORDER BY s