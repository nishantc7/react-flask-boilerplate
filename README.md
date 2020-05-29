# React Flask BoilerPlate
[![Build Status](https://travis-ci.com/nishantc7/coding-platform.svg?token=keXQyTpyLgpVLT7cyS2Q&branch=master)](https://travis-ci.com/nishantc7/coding-platform)

### A boilerplate to kickstart a fullstack project with Flask and ReactJS  

## Services  
- React Client at `/`
- Flask at `/user/`
- PostgreSQL Database
- Nginx for routing requests to flask

## Features
- Containerized with docker
- Basic User Model 
- JWT Auth Setup 
- Made different Configs for development, production and testing
- Setup Flask CORS and Database Migrations
- Test coverage for flask with Codecov
- Client side routing with React
- Bootstraped React  
- Commands to recreate `manage.py recreatedb` and setup database `manage.py seeddb`
# Steps to Reproduce
1. Clone this repository
2. Export Environment Variable with the command
`export REACT_APP_USERS_SERVICE_URL=http://0.0.0.0` or your localhost for docker-machine
3. Run the following steps in docker container
```
docker-compose up -d
python manage.py recreatedb
```
### Instance should be deployed at localhost, try by adding a new user.

##### This was made as an effort only to learn containerization and routing.


