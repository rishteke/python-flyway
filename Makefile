#!/bin/bash
help : 
	@echo "info     -- > Show current migrated ddl versions."
	@echo "migrate  -- > apply changes to database and schema "
	@echo "repair   -- > repair migration for database and schema "
	@echo "baseline -- > create script for existing database and make it baseline for future migrations."
	@echo "options  -- > flyway commandline options"

setup :
	echo "removing old _venv";
	rm -rf ./_venv;
	echo "creating python venv ";
	python3.10 -m venv _venv;
	echo " installing packages";
	_venv/bin/pip install -r requirements.txt
	echo "installed packages"

migrate:
	_venv/bin/python3.10 -m flyway-wrapper -d flywaydbtest -s test1 -fc migrate 

repair:
	_venv/bin/python3.10 -m flyway-wrapper -d flywaydbtest -s test1 -fc repair 

info:
	_venv/bin/python3.10 -m flyway-wrapper -d flywaydbtest -s test1 -fc info

baseline:
	_venv/bin/python3.10 -m flyway-wrapper -d adventureworks -s adventureworks -fc baseline
	echo " Above command is only executed in local mode as its creates new folder with files . Make sure push your changes to git."
options:
	_venv/bin/python3.10 -m flyway-wrapper -h
