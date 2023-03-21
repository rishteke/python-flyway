#!/bin/bash
hello : 
	@echo "Hello, World"

setup :
	echo "removing old _venv";
	rm -rf ./_venv;
	echo "creating python venv ";
	python3.10 -m venv _venv;
	echo " installing packages";
	_venv/bin/pip install -r requirements.txt
	echo "installed packages"

migrate:
	_venv/bin/python3.10 -m flyway-mysql -d flywaydbtest -s test1 -fc migrate 

repair:
	_venv/bin/python3.10 -m flyway-mysql -d flywaydbtest -s test1 -fc repair 

info:
	_venv/bin/python3.10 -m flyway-mysql -d flywaydbtest -s test1 -fc info

options:
	_venv/bin/python3.10 -m flyway-mysql -h
