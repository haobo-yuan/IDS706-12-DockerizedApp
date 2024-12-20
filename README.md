![CI/CD Pipeline](https://github.com/haobo-yuan/IDS706-12-DockerizedApp/actions/workflows/main.yml/badge.svg)

# IDS-706 Data Engineering: Project 12

This repository contains the week 12 project for IDS-706, focusing on creating a simple Python application containerized with Docker. The primary objectives are to demonstrate running the application within a Docker container using docker run commands and to build a Docker image as part of a CI/CD pipeline, which is then pushed to Docker Hub or another container management service.

The project showcases a fully integrated CI/CD workflow using GitHub Actions for automated building, linting, testing, and deployment of the Docker image to Docker Hub.

## Useful Links

- Docker Hub Repository: haoboyuanduke/ids706-12-dockerizedapp
> https://hub.docker.com/r/haoboyuanduke/ids706-12-dockerizedapp

---

## Features
- Containerized Python application for consistency and portability
- Automated CI/CD pipeline using GitHub Actions
- Linting, testing, and building tasks defined in the workflow
- Docker image automatically pushed to Docker Hub upon successful tests

## Setup Instructions

### Prerequisites
- Docker installed on your machine
- Python 3.x installed locally
- A GitHub and Docker Hub account

### Steps to Set Up Locally

1. **Clone the repository**:
    ```bash
    <!-- git clone https://github.com/your-username/your-repository.git -->
    git clone https://github.com/haobo-yuan/IDS706-12-DockerizedApp.git

    <!-- cd your-repository -->
    cd IDS706-12-DockerizedApp
    ```

2. **Build the Docker image**:
    ```bash
    <!-- docker build -t your-username/your-repository:latest . -->
    docker build -t ids706-12-dockerizedapp .
    ```

3. **Run the container**:
    ```bash
    <!-- docker run -it your-username/your-repository:latest -->
    docker run --rm ids706-12-dockerizedapp
    ```

### Steps to run with Docker

1. **Pull the Docker image**:
    ```bash
    docker pull haoboyuanduke/ids706-12-dockerizedapp
    ```

2. **Run the container**:
    ```bash
    docker run --rm haoboyuanduke/ids706-12-dockerizedapp
    ```

---

## AAPL Price Statistics (2010-2021)

This project calculates the mean, median,and standard deviation of AAPL stock close prices from 2010 to 2021.

![Logo Nasdaq](pictures/Logo_Nasdaq.png)![Logo AAPL](pictures/Logo_AAPL.png)

The data is from the everyday close price of <NASDAQ 100 Data From 2010> dataset on Kaggle.
>https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data/data 

The statistics are as follows:
|   Year |      mean |    median |       std |
|-------:|----------:|----------:|----------:|
|   2010 |   9.28009 |   9.18089 |  1.3413   |
|   2011 |  13.0002  |  12.7509  |  0.925852 |
|   2012 |  20.5732  |  20.8032  |  2.39203  |
|   2013 |  16.8798  |  16.467   |  1.60314  |
|   2014 |  23.0662  |  23.475   |  3.34282  |
|   2015 |  30.01    |  30.075   |  1.92089  |
|   2016 |  26.151   |  26.4375  |  1.91019  |
|   2017 |  37.6378  |  38.185   |  3.6553   |
|   2018 |  47.2634  |  46.5125  |  5.14847  |
|   2019 |  52.064   |  50.7537  |  8.63474  |
|   2020 |  95.3471  |  91.6325  | 21.8098   |
|   2021 | 134.344   | 132.42    |  9.86899  |## Description and Conclusion:


![Plot](pictures/plot.png)

### Description and Conclusion:
Apple Inc.'s stock performance from 2010 to 2021 shows significant growth, with the average
price rising from $9.28 to $134.34. The company saw consistent increases in stock value, 
particularly in 2020 and 2021, likely driven by strong demand for electronics during the pandemic
and its market leadership in innovation. While volatility increased in the later years, especially
in 2020 with the standard deviation peaking at 21.81, Apple's overall performance was robust,
reflecting its resilience and growth in the global tech industry.


## Reference

Simple python docker dev example for the official docker docs
> https://docs.docker.com/language/python/containerize/
> https://docs.docker.com/guides/language/python/configure-ci-cd/

Python Project Scaffold and Makefile Setup, from coursera by Prof. Gift
> https://www.coursera.org/videos/cloud-computing-foundations-duke/dxL50?query=scaffold&source=search
