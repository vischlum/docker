FROM debian

RUN apt-get update && apt-get install -y rails

ONBUILD EXPOSE 3000
ONBUILD COPY . /opt/app
ONBUILD WORKDIR /opt/app
ONBUILD RUN bundle install && rails db:migrate && rails db:seed
