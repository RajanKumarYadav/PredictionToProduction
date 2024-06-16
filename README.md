# Docker Image Creation for Flask ML APP


## Workflows

1. Create app directory 
2. Update or Copy paste all your files (Flask App, Trained Model, config files)
3. Create requirements.txt with all your dependencies
4. Create Docker file


# How to Run ?


Clone the repository

### STEP 01- Create a docker Image with tag

```bash
docker build -t diabetes_prediction_app:0.0.1 .
```


### STEP 02- Run the Image

```bash
docker run -p 5000:5000 diabetes_prediction_app:0.0.1
```

# Basic Docker Command

```bash
# To see all the images present in your machine
docker images
```

```bash
# To see all the running containers in your machine
docker ps -a
```

```bash
# To stop a running container
docker stop <container_id>
```

```bash
# To remove/delete a docker container(only if it stopped).
docker rm <container_id>
```

```bash
# To see the list of all the available images with their tag, image id, creation time and size.
docker image ls
```

```bash
# To delete a specific image
docker rmi <image_id>
```

```bash
# To delete a docker image forcefully
docker rmi -f <image_id>
```

```bash
# To delete all the docker container available in your machine
docker rm -f (docker ps -a | awk '{print$1}')
```

```bash
# To delete a specific image
docker image rm <image_name>
```