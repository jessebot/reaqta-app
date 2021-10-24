## To Test Locally (Outside of Docker)
``` sh
./flask_start.sh
```

### Website
Then go to http://localhost:5000 in a web browser.

### API endpoints
``` sh
curl localhost:5000/api
```

## To Test entire Docker Image

### Build the App
_Hint: you can replace 0.0.1 with whatever version you're actively testing_
``` sh
docker build -t reaqta:0.0.1 .
```

### Run the App
This will run the container and forward the container port (5000) to the standard http port (80)
``` sh
docker run --publish 5000:80 -t reaqta:0.0.1
```
