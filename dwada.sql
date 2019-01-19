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
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (1,'Cory',36,'APR',560404,8887766495,'cory@gmail.com',200000,'10','B6:53:21:30');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (2,'Josiah',42,'Palm Meadows',440937,6453867201,'josiah@gmail.com',195000,'10','36:50:32:05');
INSERT INTO `Employee` (ID,Name,Age,Adress,Zip,Phone,Email,Salary,Bonus,TagID) VALUES (3,'Fred',31,'0',0,0,'fred@gmail.com',310000,'10','B6:63:33:05');
CREATE TABLE "Carbon" (
	`emp_ID`	INTEGER NOT NULL,
	`Day`	INTEGER NOT NULL,
	`Month`	INTEGER NOT NULL,
	`Year`	INTEGER NOT NULL,
	`Mode`	VARCHAR(1000) NOT NULL,
	`CF`	INTEGER NOT NULL
);
COMMIT;
