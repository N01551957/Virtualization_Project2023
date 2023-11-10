-- Virtualization_project --

create database Virtualization_project;

CREATE TABLE Virtualization_project.todo_list (
    task_id INT(10) PRIMARY KEY auto_increment,
    task_name VARCHAR(40),
    task_date datetime default now(),
    details VARCHAR(50) default null
);
