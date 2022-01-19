FROM node:17.3-alpine as builder

RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY fourSeasonWeb/package.json fourSeasonWeb/package-lock.json /app/fourSeasonWeb/

# Install app dependencies.
RUN npm install --prefix fourSeasonWeb

# Copy app files.
COPY . /app

# Build app
RUN npm run build --prefix fourSeasonWeb -- --output-path=./dist/out

### Stage 2: delivery ###

FROM nginx:1.15.7-alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy output directory from builder to nginx image.
COPY --from=builder /app/fourSeasonWeb/dist/out /usr/share/nginx/html

# Copy nginx configuration file.
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf