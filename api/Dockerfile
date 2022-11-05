###########
# BUILDER #
###########

# pull official base image
FROM python:3.11 AS builder

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set work directory
WORKDIR /opt

# install python dependencies
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .

# PIPENV_VENV_IN_PROJECT=1 sets the .venv folder for packages
# -d to install the dev-requirements section
RUN PIPENV_VENV_IN_PROJECT=1 pipenv sync -d

###########
#  FINAL  #
###########

# pull official base image
FROM python:3.11-slim

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set timezone
ENV TZ="Europe/Moscow"

# create directory
ENV APP_HOME=/home/api/backend
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/assets/resources
RUN mkdir $APP_HOME/assets/media
RUN mkdir $APP_HOME/assets/static
WORKDIR $APP_HOME

# create appuser
RUN addgroup --system appgroup && adduser --system appuser && adduser appuser appgroup

# install dependencies
RUN apt-get update && apt-get install -y netcat

# copy virtual environment and necessary binaries
COPY --from=builder /opt/.venv /opt/.venv

# set path for virtual environment
ENV PATH="/bin:/opt/.venv/bin:$PATH"

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

ARG UPDATE_ARG=unknown
RUN UPDATE_ARG=${UPDATE_ARG}

# copy project
COPY . $APP_HOME

# chown all the files to the appuser
RUN chown -R appuser:appgroup $APP_HOME

# change to the appuser
USER appuser

# run entrypoint.sh
ENTRYPOINT ["/home/api/backend/entrypoint.sh"]
