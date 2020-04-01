SELECT count(*) FROM (
		SELECT DISTINCT docid FROM frequency WHERE (UPPER(term) = "LAW" AND count >= 1) OR (UPPER(term) = "LEGAL" AND count >= 1)
		) x;