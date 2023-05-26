FROM  registry.cn-hangzhou.aliyuncs.com/modelscope-repo/modelscope:ubuntu20.04-py37-torch1.11.0-tf1.15.5-1.5.0

EXPOSE 50051
RUN mkdir -p /usr/local/bin/service
COPY ./service /usr/local/bin/service
RUN python /usr/local/bin/service/docker_init.py # 预下载模型
RUN mkdir -p /usr/local/bin/service/cache
CMD [ "python", "/usr/local/bin/service/service.py" ]
WORKDIR /usr/local/bin/service/