BEGIN TRANSACTION;
CREATE TABLE "Employee" (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`Name`	VARCHAR(100),
	`Age`	INTEGER,
	`Adress`	VARCHAR(100000),
	`Zip`	INTEGER,
	`Phone`	INTEGER,
	`Email`	VARCHAR(1000),
	`Salary`	INTEGER,
	`Bonus`	VARCHAR(1000),
	`TagID`	INTEGER
);
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (1,'Cory Norman',36,'Adarsh Palm Retreat',560404,8887766495,'cory@gmail.com',200000,'10','B6:53:21:30');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (2,'Josiah Hicks
',42,'Palm Meadows',440937,7549245551,'josiah@gmail.com',195000,'10','36:50:32:05');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (3,'Freddy Christopher',31,'Prestige Shantiniketan',945544,9946526548,'fred@gmail.com',310000,'10','B6:63:33:05');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (4,'Jerry Vargas',46,'Prestige Ozone',485621,9985462525,'vargas.jerry@gmail.com',210000,'10','46:C7:5E:05');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (5,'Hector Lee',35,'Epsilon',542611,9854682137,'hectorlee@gmail.com',300000,'10','C3:96:C9:83');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (6,'Elsie Thorne',29,'Windmills of Your Mind',878785,7845261589,'elsie1990@gmail.com',450000,'10','D6:AB:F9:2F');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (7,'Cora Steele',31,'Prestige Lakeside Habitat',846225,7859632690,'corasteele@gmail.com',210000,'10','26:AD:20:05');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (8,'Esther Hoffman',53,'Salarpuria Sattva Luxuria',840221,9900256400,'hoffman.esther@gmail.com',510000,'10','86:D8:58:05');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (9,'Gemma Byrne',46,'Sonestaa iWoods',723516,9009564245,'gemma1973@gmail.com',470000,'10','B6:ED:F3:04');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (10,'Iqra Estrada',23,'Prestige Park Square',458261,7095642055,'estradaiqra@gmail.com',150000,'10','36:8F:56:05');
CREATE TABLE `Carbon` (
	`emp_ID`	INTEGER NOT NULL,
	`Day`	INTEGER NOT NULL,
	`Month`	INTEGER NOT NULL,
	`Year`	INTEGER NOT NULL,
	`Mode`	VARCHAR(1000) NOT NULL,
	`Model`	VARCHAR(1000) NOT NULL,
	`CF`	INTEGER NOT NULL
);
COMMIT;
