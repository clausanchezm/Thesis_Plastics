# Thesis_Plastics

Building docker image
```
docker build . -t plastics
```

Running the contqiner
```
docker run -it -p 8888:8888 -v C:\Users\33789\OneDrive\Documents\DKE\GIT\Thesis_Plastics:/tf/thesis_plastics plastics 

```

seeing what images you have 

```
docker image ls
```

seeing what container are running 

```
docker ps -a 
```
look at ps to get the name of ocntainer 
```
docker exec -it (containername) bash

 docker exec -it kind_cray bash