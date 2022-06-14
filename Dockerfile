FROM node:fermium-alpine

ARG NODE_ENV

# Env
ENV TIME_ZONE=Asia/Hong_Kong
ENV NODE_ENV $NODE_ENV

# Create Directory for the Container
WORKDIR /usr/src/app

# Only copy the package.json file to work directory
COPY package.json .
COPY package-lock.json .

# Install all Packages
RUN npm install -g typescript
RUN npm install

# Copy all other source code to work directory
ADD . /usr/src/app

# TypeScript type check and build
RUN ["tsc", "--noEmit",  "-p", "./tsconfig.json"]
RUN npm run build

# Start
CMD [ "npm", "start" ]
EXPOSE 8080
