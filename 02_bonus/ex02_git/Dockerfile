FROM	debian:stretch

RUN		apt-get update && apt-get install -y \
		git \
		vim
ARG		GIT_NAME=Vincent Schlumberger
ARG		GIT_EMAIL=vischlum@student.le-101.fr
RUN		git config --global user.name $GIT_NAME && \
		git config --global user.email $GIT_EMAIL

CMD		["sh"]

# Build with: docker build  --build-arg GIT_NAME=vischlum --build-arg GIT_EMAIL=vischlum@gmail.com -t git
# Launch it with: docker run -ti git
# And check the configuration with: git config --list
# ARG sets an environment variable only available during buildtime
