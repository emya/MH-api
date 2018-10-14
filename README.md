# MH-api

1. Docker build
```
dockebuild -t mh-api .
```

2. Docker run
```
dockerun -p 5000:5000 -e POSTGRES_HOST=<host> -e POSTGRES_PASSWORD=<password> --network myNetwork  mh-api
```