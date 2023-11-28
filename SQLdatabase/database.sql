-- Virtualization_project --

create database Virtualization_project;
use Virtualization_project;

CREATE TABLE Virtualization_project.todo_list (
    task_id INT(10) PRIMARY KEY auto_increment,
    task_name VARCHAR(40),
    task_date datetime default now(),
    details VARCHAR(50) default null
);

INSERT INTO Virtualization_project.todo_list(task_name,task_date,details)
VALUES ("testing","2023-01-01","project");
