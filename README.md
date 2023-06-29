# Predicting Elasticity of Binary Plastic Blends Through Feature Selection
### Claudia Sanchez Munoz, Bachelor Thesis, DACS UM

The project has two main parts. Filtering input features and predicting elasticity with Gaussian Processes.  
Firstly, partitions.py must be run to retrieve all partition assessed in the study. Set the local folder where to save data partitions.      
4 out the 5 filters methods are done in MATLAB: filtering.m .   
Permutation filter is done in Python. It is needed to first run permutation_importance.py, save the resulting CSV file in a path and set the path in filtering.m where table PER is read at the beginning of the file.  

## Python 
The only files to run are firstly partitioning.py and after setting the path to save the file run permutation_importance.py  
The thesis_notebook contains the initial analysis (but can be disregarded)

### Dependencies
    - Docker
### Running Code 
By running the project on Docker, all Python depedencies are automatically resolved
Let %path be the directory where repository is located.
    
Building docker image calles plastics
```
docker build . -t plastics
```

Running the container
```
docker run -it -p 8888:8888 -v %path:/tf/thesis_plastics plastics 

```

Seeing what images you have currently running

```
docker image ls
```

Seeing what container are running 

```
docker ps -a 
```
Retrieve (containerName) from ps to get the name of container to be runned and execute
```
docker exec -it (containerName) bash

````
Get partitions and  to save results of Permutation. 
```
python3 partitions.py 
python3 permutation_importance.py

````

## MatLab 
The only files to run are filtering- and gp_filters.mlx         A baseline model is included. The data exploration is done in testing_dist.mlx. The initial configurations of the library were attempted in the file gaussian_process.mlx, kept in case it is helpful. 

### Dependencies 
    - Matlab 7x and later
    - Gaussian Process Library from C. Rasmussen and H. Nickisch, https://gaussianprocess.org/gpml/code/matlab/doc/

### Set Up 
    - Download the library and place it in a folder
    - Set the Matlab Environment Path for the library :  Home - Environment - Set Path - add path of folder
    - Add all subfolders into environment. 
Having set where to find the CSV file of permutation filter, set also where to save the aggregated results in filtering 
### Running
    -run filtering.mlx 
    -run gp_filters.mlx
