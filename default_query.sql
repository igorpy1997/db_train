-- Вставка 25 книг
INSERT INTO application_book (name, pages, price, rating, publisher_id, pubdate)
VALUES
    ('Insomnia', 500, 29.99, 4.5, 1, '2022-01-01'),
    ('The Shining', 400, 39.99, 4.8, 1, '2022-02-01'),
    ('Les Misérables', 1200, 24.99, 4.2, 2, '2022-03-01'),
    ('War and Peace', 1400, 49.99, 4.7, 3, '2022-04-01'),
    ('Crime and Punishment', 600, 19.99, 4.3, 3, '2022-05-01'),
    ('Pride and Prejudice', 350, 34.99, 4.6, 4, '2022-06-01'),
    ('To Kill a Mockingbird', 400, 27.99, 4.4, 5, '2022-07-01'),
    ('1984', 300, 44.99, 4.9, 6, '2022-08-01'),
    ('The Great Gatsby', 250, 31.99, 4.2, 7, '2022-09-01'),
    ('One Hundred Years of Solitude', 500, 29.99, 4.5, 8, '2022-10-01'),
    ('Moby-Dick', 700, 39.99, 4.8, 9, '2022-11-01'),
    ('The Catcher in the Rye', 350, 24.99, 4.2, 10, '2022-12-01'),
    ('The Lord of the Rings', 1200, 49.99, 4.7, 11, '2023-01-01'),
    ('Harry Potter and the Philosopher Stone', 400, 19.99, 4.3, 12, '2023-02-01'),
    ('The Chronicles of Narnia', 350, 34.99, 4.6, 13, '2023-03-01'),
    ('Brave New World', 300, 27.99, 4.4, 14, '2023-04-01'),
    ('The Hobbit', 250, 44.99, 4.9, 15, '2023-05-01'),
    ('The Odyssey', 500, 29.99, 4.5, 16, '2023-06-01'),
    ('Hamlet', 400, 39.99, 4.8, 17, '2023-07-01'),
    ('Alices Adventures in Wonderland', 1200, 24.99, 4.2, 18, '2023-08-01'),
    ('The Picture of Dorian Gray', 1400, 49.99, 4.7, 19, '2023-09-01'),
    ('The Brothers Karamazov', 600, 19.99, 4.3, 20, '2023-10-01'),
    ('Don Quixote', 350, 34.99, 4.6, 21, '2023-11-01'),
    ('The Divine Comedy', 400, 27.99, 4.4, 22, '2023-12-01'),
    ('Frankenstein', 300, 44.99, 4.9, 23, '2024-01-01'),
    ('The Adventures of Tom Sawyer', 250, 31.99, 4.2, 24, '2024-02-01'),
    ('Wuthering Heights', 500, 29.99, 4.5, 25, '2024-03-01');

-- Вставка авторов
INSERT INTO application_author (name, age)
VALUES
    ('Stephen King', 73),
    ('Victor Hugo', 78),
    ('Leo Tolstoy', 82),
    ('Fyodor Dostoevsky', 59),
    ('Jane Austen', 41),
    ('Harper Lee', 89),
    ('George Orwell', 46),
    ('F. Scott Fitzgerald', 44),
    ('Gabriel Garcia Marquez', 87),
    ('Herman Melville', 72),
    ('J.D. Salinger', 91),
    ('J.R.R. Tolkien', 81),
    ('J.K. Rowling', 56),
    ('C.S. Lewis', 64),
    ('Oscar Wilde', 46),
    ('Miguel de Cervantes', 69),
    ('Dante Alighieri', 56),
    ('Friedrich Nietzsche', 55),
    ('Mark Twain', 74),
    ('Emily Bronte', 30);


INSERT INTO application_book_authors (book_id, author_id)
VALUES
    (1, 16),   -- Insomnia - Stephen King
    (2, 16),   -- The Shining - Stephen King
    (3, 17),   -- Les Misérables - Victor Hugo
    (4, 18),   -- War and Peace - Leo Tolstoy
    (5, 19),   -- Crime and Punishment - Fyodor Dostoevsky
    (6, 20),   -- Pride and Prejudice - Jane Austen
    (7, 21),   -- To Kill a Mockingbird - Harper Lee
    (8, 22),   -- 1984 - George Orwell
    (20, 26),  -- Alice's Adventures in Wonderland - Lewis Carroll
    (21, 30),  -- The Picture of Dorian Gray - Oscar Wilde
    (22, 19),  -- The Brothers Karamazov - Fyodor Dostoevsky
    (23, 31),  -- Don Quixote - Dante Alighieri
    (24, 32);  -- The Divine Comedy - Dante Alighieri