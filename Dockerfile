FROM docker.io/continuumio/miniconda3:4.8.2

COPY environment.yml environment.yml
RUN conda env create -f environment.yml -n deploy -q \
&& conda clean -afy

# make this new environment the default
ENV CONDA_DEFAULT_ENV=deploy
ENV CONDA_PREFIX=/opt/conda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH

WORKDIR /app

COPY src src
COPY setup.py setup.py
COPY setup.cfg setup.cfg
COPY README.md README.md

RUN pip install --no-cache-dir .

CMD ["demo_server"]
