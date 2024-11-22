-- create database RailwayDB;
drop table User_table;
drop table MasterList_table;
drop table Ticket_info_table;
drop table SeatAvl_table;
drop table Price_table;


create table User_table (
user_id varchar(255) not null,
user_name varchar(255) not null,
pass_word varchar(255) not null,
role_of_user varchar(255),
phone_num int not null,
email varchar(255)
);

create table Train_table (
train_no int not null,
train_name varchar(255) not null,
from_station varchar(255) not null,
to_station varchar(255) not null,
arrival_time varchar(255),
departure_time varchar(255),
initial_avl int,
route json,
running_dates json,
primary key (train_no,train_name)
);

create table MasterList_table (
passenger_id varchar(255) not null,
passenger_name varchar(255) ,
age int not null ,
dob varchar(255) not null,
gender varchar(255),
primary key(passenger_id)
);

create table Ticket_info_table (
pnr_no varchar(255) not null,
seat_no int,
seat_category varchar(255),
booking_date varchar(255),
passenger_id varchar(255),
passenger_name varchar(255),
age int,
train_no int,
train_name varchar(255),
ticket_status varchar(255),

foreign key (passenger_id) references MasterList_table(passenger_id),
foreign key (train_name) references Train_table(train_name),
foreign key (train_no) references Train_table(train_no)

);

create table SeatAvl_table (
train_no int not null,
train_name varchar(255),
sleeper int default(0) ,
seating int default(0),
third_ac int default(0),
second_ac int default(0),
first_ac int default(0),
foreign key (train_name) references Train_table(train_name),
foreign key (train_no) references Train_table(train_no)

);

create table Price_table (
train_no int not null,  
train_name varchar(255),
sleeper_price int default(0) ,
seating_price int default(0),
third_ac_price int default(0),
second_ac_price int default(0),
first_ac_price int default(0),
foreign key (train_name) references Train_table(train_name),
foreign key (train_no) references Train_table(train_no)

);



alter table Train_table add index (train_no);
alter table Train_table add index (train_name);
insert into User_table values ("Kishore10","Kishore Babu","kish10","admin",9176435578,"kishore@gmail.com");
insert into User_table values ("Stark10","Stark","stark10","admin",78,"stark@gmail.com");
insert into Train_table values (123456,"uzhavan","Tambaram","Thanjavur","22:40","6:00",130,'["Route A", "Route B", "Route C"]','["M","T","w","F"]');
insert into MasterList_table values ("3376435567","Kishore Babu",18,"2005-10-01","male");
insert into Ticket_info_table values ("22334456P",13,"SL","2024-11-01","3376435567","Kishore Babu",18,123456,"uzhavan","booked");

select user_name, pass_word from User_table;




