show databases;
create database ipv;
use ipv;

create table desk_data(
stock_name varchar(50),
qty int,
desk_price int);

create table independent_prices(
stock_name varchar(50),
independent_price int);

insert into desk_data values ('Reliance',20,2500),('TCS',10,3000),('Kotak',50,2400),('Bajaj',50,1600),('LIC',40,7800);
insert into independent_prices values ('Reliance',2550),('TCS',3100),('Kotak',2600),('Bajaj',1700),('LIC',8000);

select* from desk_data;
select* from independent_prices;


