# A guide to the server stuff

# Docker

### Explanation
Dockerfile in this repository allows to create a docker container with all required software to run students' notebooks. This container is using nvidia-docker stuff for cuda purposes

### Building

To build an image run following code near the Dockerfile

```docker build --rm -t <image_name> .```

For example:

```docker build --rm -t mrartemev/mlhep_students .```

### Usage
To run docker image run following code inside repo directory

```docker run --rm -v `pwd`:/workdir --name <name> --runtime nvidia -it -p <port>:8888 <image_name>```

For example:

```docker run --rm -v `pwd`:/workdir --name my_project --runtime nvidia -it -p 7777:8888 mrartemev/mlhep_students```

Running this command will mount docker to your repo directory and execute jupyter notebook command inside your docker.

Open this in your browser to work with repo http://localhost(or yours server-id):8888 (or other chosen <port>). After that, you'll be able to run ipython notebooks

Once you finished just do usual `git add`, `git commit -m`, `git push` routine to commit changes to the repo

I recommend to run this docker image in something like tmux or screen just in case

If something goes wrong ping me @mrartemev






