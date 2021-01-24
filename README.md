# No-Reference Image Quality Assessment (Mobit)

This is my practical test for Embedded Systems developer at Mobit LTDA.

Author: Otávio A. M. Guerra

## Steps to setup and execute the test aplication

1) Clone this repository

2) Install [docker](https://www.docker.com/)

3) Build the project:
```bash
docker-compose build
```
4) Run:
```bash
docker-compose run
```
5) Go to `localhost:8501` to use the UI to test the application.

6) [Optional]: Go to `localhost:8000` to see REST API documentation

## Project structure and architecture

The project has the following architecture:

![Project Architecture](Project-Architecture.png)

OBS1: The quality score computes the [BRISQUE](https://live.ece.utexas.edu/publications/2012/TIP%20BRISQUE.pdf) score for any given image.

OBS2: The distortion classification service was NOT developed due to insufficient time.

## Final result

![Application GIF](Application-GIF.gif)
