-- lists all Comedy shows in the database hbtn_0d_tvshows

SELECT s.title
FROM tv_shows AS s
	INNER JOIN tv_show_genres as t
	ON t.show_id = s.id

	INNER JOIN tv_genres as g
	ON g.id = t.genre_id
	WHERE g.name = "Comedy"
ORDER BY s.title;
