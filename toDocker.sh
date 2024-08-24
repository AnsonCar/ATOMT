docker build --platform linux/amd64 -t ansoncar/atomt:v .
# docker tag ansoncar/atomt:v$1 ansoncar/atomt:v$1
# docker push ansoncar/atomt:v
# docker pull ansoncar/atomt:v3.2.3
docker run -d -p 5004:5004 ansoncar/atomt:v