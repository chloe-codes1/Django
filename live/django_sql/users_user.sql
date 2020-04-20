--users_user
CREATE TABLE IF NOT EXISTS "users_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "first_name" varchar(10) NOT NULL, 
    "last_name" varchar(10) NOT NULL, 
    "age" integer NOT NULL, 
    "country" varchar(10) NOT NULL, 
    "phone" varchar(15) NOT NULL, 
    "balance" integer NOT NULL
    );

-- .read users_user.sql