# <h1>Library Management</h1>

        This project is about library management with gRPC backend, postgress databse and React Frontend. With React Redux, Hooks, Router, gRPC Web modules included. 

        Used python code generation tools protoc, and npm tools protoc-gen-js,protoc-gen-grpc-web buffers for generating gRPC from proto templates with basic implementation. 

        React to communicate to python gRPC server it require grpc-web support proxy like envoy. Ngnix on windows require to be build with gRpc Web Support. 

        Javascript gRPC Web generated files make grpweb call, it needs to proxied to envoy grpc web. envoy grpc web will connect to grpc native server over tcp with binary or encoded data. 

## 1. Main Screen<p>
![Alt text](/screenshots/1.png?raw=true "Main Screen")

## 2. Create Book<p>
![Alt text](/screenshots/2.png?raw=true "Create Book")

## 3. Create Book Validation with react-hook-form<p>
![Alt text](/screenshots/3.png?raw=true "Create Book Validation")

## 4. Update Book <p>
![Alt text](/screenshots/4.png?raw=true "Update Book")

## 5. Create Member <p>
![Alt text](/screenshots/5.png?raw=true "Create Member")

## 6. Update Member <p>
![Alt text](/screenshots/6.png?raw=true "Update Member")

## 7. List Book Transaction <p>
![Alt text](/screenshots/7.png?raw=true "List Book Transaction")

# <h2>Steps for Setup.<h2>

## Install python

# Install required packages
        python -m pip install grpcio grpcio-tools

## Generate the Python files

        python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. book.proto 

        python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. member.proto

        python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. book_transaction.proto

### or with packaged files
        python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=.. book/proto/book.proto


## start book server, client and request with client
        start python book_server.py
        python book_client.py

## start member server and request with client
        start python member_server.py
        python member_client.py

## start book_transaction server and request with client
        start python book_transaction_server.py
        python book_transaction_client.py

## Generate JavaScript/TypeScript Client Code 
### Command for generating grpc-web JS code (requires protoc and the grpc-web plugin)
    #### install protoc-gen-js protoc-gen-grps-web
        npm install -g protoc-gen-js
        npm install -g protoc-gen-grpc-web

    #### generate js for proto
        # With python protoc tool --jsout binary, mode grpcwebtext
        python -m grpc_tools.protoc -I=. book.proto --js_out=import_style=commonjs,binary:. --grpc-web_out=import_style=commonjs,mode=grpcwebtext:.
        
        # With python protoc tool --jsout binary, mode grpcweb
        python -m grpc_tools.protoc -I=. book.proto --js_out=import_style=commonjs,binary:. --grpc-web_out=import_style=commonjs,mode=grpcweb:.

        or
        # With python protoc tool --jsout binary,mode grpcweb
        python -m grpc_tools.protoc -I=. book.proto --js_out=import_style=commonjs:. --grpc-web_out=import_style=commonjs,mode=grpcweb:.

## install docker, envoy
    ### docker for windows download and install

    ### pull envoy image for docker
            docker pull envoyproxy/envoy:v1.33-latest
    ### start docker
            docker run --rm -it -p 9901:9901 -p 10000:10000 envoyproxy/envoy:v1.35.0

### use envoy docker config to run grpc-web proxy

        docker run --rm -p 8080:8080 -v %cd%/envoy.yaml:/etc/envoy/envoy.yaml envoyproxy/envoy:v1.35.0 envoy -c /etc/envoy/envoy.yaml --log-level info

### verify envoy url
        http://localhost:8080/


## Nginx

            start nginx
            tasklist /fi "imagename eq nginx.exe"
            nginx -s quit
            nginx -s stop

## start book server from python
            python book_server.py


## install database connectino pool library

        pip install psycopg2-binary

## response type check
        Object.getOwnPropertyNames(Object.getPrototypeOf(response))

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
