FROM debian
RUN apt-get update && apt-get install -qy bzip2 wget \
&& rm -rf /var/lib/apt/lists/*
RUN wget dl.4players.de/ts/releases/3.1.1/teamspeak3-server_linux_amd64-3.1.1.tar.bz2
RUN tar -xvf teamspeak3-server_linux_amd64-3.1.1.tar.bz2
RUN rm teamspeak3-server_linux_amd64-3.1.1.tar.bz2

WORKDIR /teamspeak3-server_linux_amd64 
#RUN sh ts3server_minimal_runscript.sh createinifile=1
# Automatically accept the license agreement
ENV TS3SERVER_LICENSE accept

# Expose the Standard TS3 port, for files, for serverquery
EXPOSE 9987/udp 30033 10011
# Launch Teamspeak on startup
ENTRYPOINT ["./ts3server_minimal_runscript.sh"]
###	TO TEST
# docker build -t ts3 .
# docker run -p=9987:9987/udp -p=30033:30033/tcp -p=10011:10011/tcp ts3
# docker-machine ip Char		(don't forget to setup the env var)
# Connect on Teamspeak using port 9987
