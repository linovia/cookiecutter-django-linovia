CREATE USER {{cookiecutter.project_name}} WITH ENCRYPTED PASSWORD '{{cookiecutter.project_name}}';
ALTER USER {{cookiecutter.project_name}} CREATEDB;

CREATE DATABASE {{cookiecutter.project_name}} owner {{cookiecutter.project_name}} encoding 'UTF8';