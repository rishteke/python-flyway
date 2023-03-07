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

run:
	_venv/bin/python3.10 -m flyway-mysql

options:
	_venv/bin/python3.10 -m flyway-mysql -h
