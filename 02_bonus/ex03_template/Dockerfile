FROM	debian:stretch

RUN		apt-get update && apt-get install -y \
		git \
		vim

# Expect a build-time variable
ARG		NEW_PROJECT=work
# Use the value to set the ENV var default
ENV		new_project=$NEW_PROJECT

#RUN		mkdir "$NEW_PROJECT"

ENTRYPOINT	git clone https://github.com/cfpb/open-source-project-template.git "$new_project" \
			&& cd "$new_project" \
			&& /bin/bash

# Launch with: docker run -e "new_project=top_secret" -it <ImageID>
# If you don't define new_project, the directory will be called "work"
# ENV sets an environment variable available during both buildtime and runtime
