# Favicon Asset Detector API

This is a simple and optimized API that takes a URL as input and returns the assets of the given URL using favicon image and lookup table.

## Installation

To use this application, you would need to have Python3 and Docker installed on your system.

1. Clone this repo 
`git clone git@github.com:eekoseoglu/favicon.git`

2. Run the app with following command inside project folder:
    - Windows : `./run.bat <number_of_workers>`
    - Linux : `docker compose up --detach --build --remove-orphans --scale app=<number_of_workers>`

This will start the FastAPI server on http://localhost:8000/my-first-api, and servers are picked up with round-robin technique for demo purposes.

## Usage
The API endpoint expects a query parameter `url` which is the URL of the website you want to get the asset information for.

Send a request or open a web browser and write to this address(https://jellyfin.org as an example):
    http://localhost:8000/my-first-api?url=https://jellyfin.org
You will receive a response in JSON format which contains presence of a specific type of product or software.

## Stopping Containers
To stop containers, simply run inside project folder:
```bash
docker compose down
```

## Running Unit Tests
To run unit tests go to `/favicon/favicon_matcher` folder and run the following command:
```bash
python -m unittest
```
