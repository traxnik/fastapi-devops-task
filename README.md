# FastAPI Docker DevOps Project

## Build Image
docker build -t get-app .

## Run Container
docker run -p 8000:8000 get-app

## Access
http://localhost:8000/user?username=test
