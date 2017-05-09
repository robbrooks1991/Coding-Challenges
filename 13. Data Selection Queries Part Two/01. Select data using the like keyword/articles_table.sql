use my_database;

/** create a new table called articles*/

create table articles(
	id integer auto_increment,
    title varchar(200),
    content text,
    person_id int not null,
    primary key (id)
);

/** insert some data into this table*/

insert into articles(
	title,
    content,
    person_id
) VALUES
    ('article 1', 'some text', 1),
    ('article 2', 'some more text', 1),
    ('article 3', 'even more text', 1),
    ('article 4', 'wow so much text', 1);