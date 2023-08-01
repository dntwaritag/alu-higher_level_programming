-- A script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
-- Query to create a second table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT);
INSERT INTO second_table (id, name, score) VALUES (1, 'Denyse', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Aline', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Benitha', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'Grace', 8);
