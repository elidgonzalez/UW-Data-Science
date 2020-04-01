SELECT count(*) FROM (
		SELECT docid FROM frequency 
		GROUP BY docid
		HAVING count(count) > 300
		) x;