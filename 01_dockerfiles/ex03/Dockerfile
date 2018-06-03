FROM ubuntu:14.04

# Install required packages
RUN apt-get update -q \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    ca-certificates \
    openssh-server \
    wget \
    apt-transport-https

# Download & Install GitLab
RUN echo "deb https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/gitlab_gitlab-ce.list
RUN wget -q -O - https://packages.gitlab.com/gpg.key | apt-key add -
RUN apt-get update && apt-get install -yq --no-install-recommends gitlab-ce

# Expose web & ssh
EXPOSE 443 80 22

# Define data volumes
VOLUME ["/etc/gitlab", "/var/opt/gitlab", "/var/log/gitlab"]

# Copy assets
COPY	script.sh /

# Wrapper to handle signal, trigger runit and reconfigure GitLab
CMD ["/script.sh"]

# Build it with: docker build -t gitlab .
# Launch it with: docker run -ti -p=443:443 -p=80:80 gitlab
# Stop it with: docker kill <container_name>
