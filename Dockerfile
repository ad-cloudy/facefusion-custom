# CUDA-enabled FaceFusion base image (already has CUDA + lots of deps ready)
FROM facefusion/facefusion:3.5.0-cuda

# Put your code here inside the container
WORKDIR /app

# Copy your custom repo into the image
COPY . /app

# Gradio must listen on 0.0.0.0 inside containers (not 127.0.0.1)
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7870
ENV GRADIO_ANALYTICS_ENABLED=False

# This tells Northflank “this container listens on 7870”
EXPOSE 7870

# Start FaceFusion UI
CMD ["bash", "start.sh"]
