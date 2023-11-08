# Development Environment Setup

- [Development Environment Setup](#development-environment-setup)
  - [Command Line Tools](#command-line-tools)
  - [Brew](#brew)
  - [VS Code](#vs-code)
  - [Python](#python)
  - [Poetry](#poetry)
  - [Pre-Commit](#pre-commit)
  - [Docker](#docker)
  - [Docker Compose](#docker-compose)
  - [Postgresql Client](#postgresql-client)

## Command Line Tools

This is a Mac Specific Step. This step will install most of the basic development dependencies on mac, like git, make.

Make sure to upgrade your macOs Version before installing this.


#### Install <!-- omit in toc -->
```sh
xcode-select –install
```

#### Verify <!-- omit in toc -->
```sh
git --version
```
```
git version 2.32.0 (Apple Git-132)
```

## Brew

Homepage: https://brew.sh/

#### Install <!-- omit in toc -->

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Verify <!-- omit in toc -->

```sh
brew --version
```
```
Homebrew 3.3.9-103-ga0ae4a7
Homebrew/homebrew-core (git revision fda2f1d6a09; last commit 2022-01-03)
Homebrew/homebrew-cask (git revision 76117c739f; last commit 2022-01-03)
```

## VS Code

Most of us use VS Code for the codebase.

#### Install <!-- omit in toc -->
You can use brew to install VS Code

```sh
brew install --cask visual-studio-code
```

Alternatively, you can download the dmg from [VS Code website](https://code.visualstudio.com/).

#### Verify  <!-- omit in toc -->
```sh
code --version
```
```
1.63.2
899d46d82c4c95423fb7e10e68eba52050e30ba3
x64
```

## Python

Recommended version of Python is 3.10 and above.

The Production servers are running in Python 3.10.

#### Install <!-- omit in toc -->

```sh
brew install python@3.10
```

#### Verify <!-- omit in toc -->
```sh
python3 --version
```
```
Python 3.10.6
```

## Poetry

Codebase uses [Poetry](https://python-poetry.org/docs/) to manage dependencies.

#### Install <!-- omit in toc -->

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

#### Verify <!-- omit in toc -->

```sh
poetry --version
```
```
Poetry version 1.2.1
```

#### Config <!-- omit in toc -->

Need to make some config changes to make sure it creates the virtual env in the workspace

```sh
poetry config virtualenvs.in-project true
```


You can check the full configuration using the below command.

```sh
poetry config --list
```
```
cache-dir = "/Users/nean/Library/Caches/pypoetry"
experimental.new-installer = true
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = true
virtualenvs.path = "{cache-dir}/virtualenvs"  # /Users/nean/Library/Caches/pypoetry/virtualenvs
```


## Pre-Commit

We use [Pre-Commit](https://pre-commit.com/) to lint and auto-fix coding-style changes before a commit is made.


#### Install <!-- omit in toc -->

```sh
brew install pre-commit
```

#### Verify <!-- omit in toc -->

```sh
pre-commit --version
```
```
pre-commit 2.16.0
```


## Docker

We use docker to manage our non-python development dependencies, like postgres, redis.

#### Install <!-- omit in toc -->

Follow the installation instructions here at https://docs.docker.com/desktop/mac/install/


#### Verify <!-- omit in toc -->

Verify installation

```sh
docker --version
```
```
Docker version 20.10.11, build dea9396
```

Verify Docker running status

```sh
docker run hello-world
```
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete 
Digest: sha256:2498fce14358aa50ead0cc6c19990fc6ff866ce72aeb5546e1d59caac3d0d60f
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Docker Compose

We use docker-compose yaml files to setup and teardown development environments.

#### Install <!-- omit in toc -->

Latest Versions of Docker Desktop for Mac includes Compose along with other Docker apps, so Mac users do not need to install Compose separately. For installation instructions, see [Docker](#docker).

Alternatively, You can install docker-compose via brew

```sh
brew install docker-compose
```

#### Verify <!-- omit in toc -->

```sh
docker-compose --version
```
```
Docker Compose version v2.2.1
```


## Postgresql Client

The actual Postgres instance used in development is managed by docker-compose. But we have some old make commands which make use of `psql` command line client to run some setup.

#### Install <!-- omit in toc -->
```sh
brew install postgresql
```

#### Verify <!-- omit in toc -->
```sh
psql --version
```
```
psql (PostgreSQL) 14.1
```
