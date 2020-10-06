# pull official base image
FROM node:13.12.0-alpine


# install app dependencies
COPY /starter-client /usr/src/starter-client

WORKDIR /usr/src/starter-client

RUN npm install
RUN npm install react-scripts@3.4.1 -g


# start app
CMD ["npm", "start"]