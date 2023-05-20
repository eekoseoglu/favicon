@echo off

set number_of_workers=%1

if not defined number_of_workers (
    set number_of_workers=1
    @echo Running with 1 worker
) else (
    @echo Running with %number_of_workers% workers
)

docker-compose up --detach --build --remove-orphans --scale app=%number_of_workers%