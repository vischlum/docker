FROM	debian:stretch

RUN		apt-get update && apt-get install -y \
		mpv

ENTRYPOINT	mpv --ao=null --vo=tct --vo-tct-256=yes --vo-tct-algo=plain https://www.youtube.com/watch?v=dQw4w9WgXcQ
# Launch it with: docker run -it <ImageID>
# MPV options:
#	--ao-null disables audio output
#	--vo-tct enables the true-color terminal video output
#	--vo-tct-256=yes limits the output to 256 colours for performance reasons
#	--vo-tct-algo=plain limits the resolution to minimise dropped frames
