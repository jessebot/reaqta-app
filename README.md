# maybeyou.live runs this live right now

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

### Build the App using Docker
_Hint: you can replace 0.0.1 with whatever version you're actively testing_
``` sh
docker build -t reaqta:0.0.1 .
```

### Run the App in Docker
This will run the container and forward the container port (5000) to the standard http port (80)
``` sh
docker run --publish 5000:80 -t reaqta:0.0.1
```

### CICD
The only ci/cd in place right now is a basic github action that runs anytime you push up a git tag, that builds the docker image, and pushes it to a public dockerhub repo. k8s has no ci/cd, because I ran out of time, whoops

## Kubernetes

### The content in k8s needs to be a helm chart
More like goobernetes, amirite?
Anyway...
But in the meantime, you could theoretically just run a `k apply -f` for every yaml file in there, and you should be good.

It deploys:  k8s service, deployment, and namespace -- this all lives in the flaskapp namespace, for honestly no reason other than I'm sleepy

### proper gitops not functional, but SOON
we're gonna just have the image tag updated, but will first require a proper k8s ci/cd process - for now, we're just using always pull image policy, and then scaling up and down deployments - or just killing off pods, that works too.

## SSL
welp, there's none of that right now, :shrug: but we can set that up via letsencrypt if we want later
