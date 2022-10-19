FROM ubuntu
RUN mkdir workdir
RUN cd workdir
COPY ./hello.py ./
RUN apt update -y && \
        apt upgrade -y && \
           apt-get install -y wget && \
             apt install iputils-ping -y && \
                apt install -y python3 && \
                apt-get install software-properties-common -y && add-apt-repository ppa:mozillateam/ppa -y && \
                apt install -t 'o=LP-PPA-mozillateam' firefox -y

CMD ["python3", "hello.py"]

