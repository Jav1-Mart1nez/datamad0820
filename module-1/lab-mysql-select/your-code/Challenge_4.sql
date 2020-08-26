SELECT 
au.au_id AS AUTHOR_ID, au.au_lname AS LAST_NAME, au.au_fname AS FIRST_NAME,
COALESCE (null, sum(sa.qty),0) AS TOTAL
FROM publications.authors AS au
LEFT JOIN publications.titleauthor AS tiau ON au.au_id = tiau.au_id
LEFT JOIN publications.titles AS ti ON tiau.title_id = ti.title_id
LEFT JOIN publications.sales AS sa ON ti.title_id = sa.title_id
GROUP BY au.au_id, au.au_lname, au.au_fname
ORDER BY TOTAL DESC;

