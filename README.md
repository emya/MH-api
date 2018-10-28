# MH-api

1. Docker build
```
docker build -t mh-api .
```

2. Docker run
```
docker run -p 5000:5000 -e POSTGRES_HOST=<host> -e POSTGRES_PASSWORD=<password> --network myNetwork  mh-api
```

3. Run postgres (for local)
```
docker run -p 5432:5432 --name mh-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=root --network myNetwork -d postgres 
```