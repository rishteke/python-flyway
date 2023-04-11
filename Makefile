#!/bin/bash
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

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
	_venv/bin/python3.10 -m flyway-wrapper -d $(database) -s $(schema) -fc migrate 

repair:
	_venv/bin/python3.10 -m flyway-wrapper -d $(database) -s $(schema) -fc repair 

info:
	_venv/bin/python3.10 -m flyway-wrapper -d $(database) -s $(schema) -fc info

ddl_dump: 
ifneq ($(wildcard ./scripts/$(database)*),)
	@echo "Folder present $(database) "
else
	@echo "Creating Folder $(database)."
	@mkdir ./scripts/$(database)
endif

ifneq ($(wildcard ./scripts/$(database)/V1__$(database).sql*),)
	@echo "file  Found V1__$(database).sql "
else
	@mysqldump -d -u $(DB_USER) -h $(DB_HOSTNAME)  $(database)  --password='$(DB_PASSWORD)'  > ./scripts/$(database)/V1__$(database).sql
	@echo "sql DDL dump successful !!! "
endif
	
baseline: ddl_dump
	@echo "initial dump completed . !! "
	@echo "Folder present $(database) "
	# _venv/bin/python3.10 -m flyway-wrapper -d $(database) -s $(schema) -fc baseline
	echo " Above command is only executed in local mode as its creates new folder with files . Make sure push your changes to git."

options:
	_venv/bin/python3.10 -m flyway-wrapper -h	