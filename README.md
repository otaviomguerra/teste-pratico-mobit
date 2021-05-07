# No-Reference Image Quality Assessment (Mobit practical test)

This is my practical test for Data Scientist role at Mobit Brasil LTDA.

Author: Otávio A. M. Guerra

## Steps to setup and execute the test application

1) Clone this repository.

2) Install [docker](https://www.docker.com/).

3) Build the project:
```bash
docker-compose build
```
4) Run:
```bash
docker-compose run
```
5) Open any web browser and access `localhost:8501` to use the UI to test the application.

6) [Optional]: Go to `localhost:8000` to see REST API documentation.

## Project structure and architecture

The project has the following architecture:

![Project Architecture](images/Project-Architecture.png)

OBS1: The quality score computes the [BRISQUE](https://live.ece.utexas.edu/publications/2012/TIP%20BRISQUE.pdf) score for any given image. See the paper for more details.

OBS2: The distortion classification service was NOT developed due to insufficient time 😕.

## Final result

![Application GIF](images/Application-GIF.gif)
