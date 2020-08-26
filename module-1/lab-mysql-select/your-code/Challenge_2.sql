SELECT 
au.au_id AS AUTHOR_ID, au.au_lname AS LAST_NAME, au.au_fname AS FIRST_NAME, 
pu.pub_name AS PUBLISHERS,
count(pu.pub_name) AS PUBLISHERS
FROM publications.authors AS au
LEFT JOIN publications.titleauthor AS tiau ON au.au_id = tiau.au_id
LEFT JOIN publications.titles AS ti ON tiau.title_id = ti.title_id
LEFT JOIN publications.publishers AS pu ON ti.pub_id = pu.pub_id
GROUP BY au.au_id
ORDER BY au.au_id DESC;