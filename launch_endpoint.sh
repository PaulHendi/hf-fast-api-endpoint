# Change those two variables to the appropriate values
CONTAINER_NAME=us-east4-docker.pkg.dev/hf-notebooks/gpu-transformers/endpoint:v1
VOLUME=~/hf-fast-api-endpoint/volume

# Configure Docker to use the gcloud command-line tool as a credential helper 
gcloud auth configure-docker us-east4-docker.pkg.dev

#Create the app directory
echo "Creating the app_mount directory ..."
mkdir -p ${VOLUME}


#Launch the container and run the training script
echo "Launching the container and starting the endpoint ..."
docker run -p 80:80 --gpus all -v ${VOLUME}:/volume ${CONTAINER_NAME} 
