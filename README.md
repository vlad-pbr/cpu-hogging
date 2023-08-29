Examples of CPU hogging
=======================

This repository contains code snippets which showcase usage of CPU as a system resource. It contains various cases of 
needless processor usage and also displays which factors can affect CPU usage by processes in general.

Made for my [Medium](https://medium.com/@vlad.pbr/three-stages-of-cpu-usage-grief-86b2238a0ddd) article.

# Usage

Code snippets are meant to be run in a container using a pre-built image, like so:
```shell
docker run --rm --name cpu-hogging -it vladpbr/cpu-hogging:python -c "from samples.tight_loop import problem; problem()"
```

Snippet behavior can then be inspected in a separate terminal using the following command:
```shell
docker stats cpu-hogging
```