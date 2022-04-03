FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

RUN pip install pytorch-lightning && \
    python -c "import pytorch_lightning" && \
    python -V && \
    python -m pip list
