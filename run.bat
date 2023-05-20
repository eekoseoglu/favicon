@echo off 


if [%1]==[] goto default

set /A number_of_workers=%1
@echo works with arguments %number_of_workers%
docker-compose up --build --remove-orphans --scale app=%1
goto :eof

:default
@echo this is default 1
docker-compose up --build --remove-orphans --scale app=1
goto :eof