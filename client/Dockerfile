# pull official base image
FROM node:13.12.0-alpine


# install app dependencies
COPY /starter /usr/src/starter

WORKDIR /usr/src/starter


# start app
CMD ["npm", "run", "dev"]