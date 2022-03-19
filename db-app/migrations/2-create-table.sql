CREATE TABLE movie (
    id char(5) CONSTRAINT firstkey PRIMARY KEY,
    title varchar(40) NOT NULL,
    genre varchar(40) NOT NULL
);