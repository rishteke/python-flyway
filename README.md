# python-flyway

## Python wrapper project for running docker flyway command for mysql database migration.

### Prerequisites

1. Docker

2. Latest Flyway docker image.

3. Mysql JDBC driver


For existing mysql database.

1. mysqldump utility. 

 

### Setup

`make setup`


Check all the options using command

`make help`

Example : Migrate changes to database 

`make migrate database=DATABASE_NAME schema=SCHEMA_NAME`