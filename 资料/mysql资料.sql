--数据库基本操作
	--连接数据库 
	mysql -uroot -p123456
	--断开数据库
	exit 、 quit 、ctrl+d
	--sql语句最后要有；分号结尾
	--查看数据库
	show databases；
	--当前时间
	select now();
	--数据库当前版本
	select version();
	---创建数据库
	--create database 数据库的名字 charset=utf8；
	create database student charset=utf8；
	--查看数据库
	--show create database 数据库名字； 查看数据库是如何创建的
	show create database student;
	--删除数据库
	--drop database 数据库名字；
	drop database student;
	--查看当前使用数据库
	select database();
	--使用某个数据库
	--use 数据库名字；
	use student；

--数据库的表操作
	--查看当前数据库里面所有的表
	show tables；
	--创建一个数据表
	-- create table 表的名字(id int ,name varchar);
	create table student(id int,name varchar(30));
	create table student(id int primary key not null auto_increment,
		name varchar(30));
	--查看一个数据表的结构
	-- desc 表的名字;
	desc student;
	--查询表里的所有数据
	-- select * from 表的名字；
	select * from student;
	--删除一个表
	-- drop table 表的名字；
	drop table student；
	--查看一个表
	show create table student;
--修改表结构
	--添加一个新的表字段
	-- alter table 表名 add 新字段 字段类型;
	alter table student add bithday datetime;
	--修改一个表字段的字段类型
	alter table student modify birthday date;
	--修改一个表字段的字段名字
	alter table student change birthday birth date defult "1996-10-06";
	--删除一个表字段
	alter table student drop high;


--增删改查
























