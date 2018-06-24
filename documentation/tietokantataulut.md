# Käytetyt tietokantataulut  



```
 CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, admin boolean, 
	PRIMARY KEY (id)
);

CREATE TABLE pen (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	country VARCHAR(144) NOT NULL, 
	manufacturer VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE collection (
	id integer, 
	date_created datetime, 
	date_modified datetime, 
	nib varchar(144), 
	color varchar(144), 
	account_id integer, 
	pen_id integer, 
	primary key (id), 
	foreign key(account_id) references account (id), 
	foreign key (pen_id) references pen (id)
);

```
