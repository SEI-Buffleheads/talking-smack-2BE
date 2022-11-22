CREATE DATABASE twitter;

CREATE USER twitter_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE twitter TO twitter_admin;

