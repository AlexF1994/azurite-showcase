FROM node:17-bullseye-slim
RUN npm install -g azurite
WORKDIR /azurite
RUN azurite-blob --blobHost 0.0.0.0 --blobPort 10000 --location /azurite --debug /azurite/debug.log
