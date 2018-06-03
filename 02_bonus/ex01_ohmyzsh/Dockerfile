FROM	debian:stretch

RUN		apt-get update && apt-get install -y wget git zsh \
		&& wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

CMD		["zsh"]
# Launch it with docker run -ti <image>
# Check the shell you're using with echo $0
