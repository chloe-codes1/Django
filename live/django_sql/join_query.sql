-- 게시글(A) + 댓글(B)
SELECT * FROM article
LEFT OUTER JOIN comment
ON article.id = comment.article_id;

-- 게시글(A) + 사용자
SELECT * FROM article
INNER JOIN user
ON article.user_id = user.id;