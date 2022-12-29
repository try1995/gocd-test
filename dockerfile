FROM mycentos:cpic

ENV myPath /app/appdata
ENV logDir /applog
ENV proConf /cpic/cpicapp
ENV conf ${proConf}/conf
ENV scripts /app/bin

ENV app ${myPath}/appxxx

# ADD xxx.zip ${myPath}
ADD requirements.txt ${myPath}
ADD start.sh ${scripts}

RUN mkdir ${app}
RUN pip3 install --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r ${myPath}/requirements.txt

EXPOSE 8080

# docker run --name appxxx --gpus=all -p 31002:8080 -v /C/Users/liubei/Documents/project/app/appxxx:/app/appdata/appxxx -it mycentos:appxxx-v1.0 /bin/bash