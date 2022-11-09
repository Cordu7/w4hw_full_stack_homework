

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    f_name VARCHAR (255),
    l_name VARCHAR (255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR (255),
    genre VARCHAR (255),
    author INT REFERENCES authors(id)
)