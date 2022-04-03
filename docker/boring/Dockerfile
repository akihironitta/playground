FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

LABEL maintainer "Akihiro Nitta <nitta@akihironitta.com>"
LABEL repository "https://github.com/akihironitta/playground"
LABEL org.opencontainers.image.description "A random image"

RUN pip install pytorch-lightning && \
    python -c "import pytorch_lightning" && \
    python -V && \
    python -m pip list
