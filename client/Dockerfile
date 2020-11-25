FROM node:13.12.0-alpine

# Set working directory
WORKDIR /srv/startr

# Install PM2 globally
RUN npm install --global pm2

# Copy package.json and package-lock.json before other files
# Utilise Docker cache to save re-installing dependencies if unchanged
COPY /startr/package.json package.json
COPY /startr/package-lock.json package-lock.json

# Install dependencies
RUN npm install --production

# Copy all files
COPY /startr ./

# Build app
RUN npm run build

# Expose the listening port
EXPOSE 3000

# Run container as non-root (unprivileged) user
# The node user is provided in the Node.js Alpine base image
USER node

# Run npm start script with PM2 when container starts
CMD [ "pm2-runtime", "npm", "--", "start" ]