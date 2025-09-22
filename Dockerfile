# Read the doc: https://huggingface.co/docs/hub/spaces-sdks-docker
# you will also find guides on how best to write your Dockerfile

FROM python:3.13-slim

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir gunicorn
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 7860

COPY --chown=user . /app
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
