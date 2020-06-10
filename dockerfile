FROM ubuntu:latest
RUN ["useradd","user"]
RUN ["usermod","-G","sudo","user"]
RUN echo "user:user" | cat > password.txt
RUN cat password.txt
RUN chpasswd < password.txt
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","git","sudo","lsb-release"]
WORKDIR /home/user
RUN ["mkdir","stwork"]
RUN ["chown","user","stwork"]
USER user
WORKDIR stwork
RUN ["git","clone","https://github.com/ArduPilot/ardupilot.git"]
WORKDIR ardupilot
RUN ["git","submodule","update","--init","--recursive"]
WORKDIR Tools
WORKDIR environment_install
CMD ["bash"]
