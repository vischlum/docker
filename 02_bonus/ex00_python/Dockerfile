FROM	debian:stretch

RUN		apt-get update && apt-get install -y \
		python3 \
		python3-pip \
		&& pip3 install pylint

CMD		["python3"]
# Test it with docker run -ti <image>
