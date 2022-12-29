#!/bin/bash
appPath="/app/appdata/xxx"
configPath="/cpic/cpicapp/conf/config.py"
modelPath="/app/appdata/xxx_models.tar"
logPath="/applog/xxx.log"
rm -rf $appPath && mkdir $appPath
# 代码文件
echo "tar code file"
tar -C $appPath -xvf $appPath.tar
chmod -R 755 $appPath
# 模型文件
echo "tar model file"
tar -C $appPath -xvf $modelPath
# 配置文件
echo "cp config file"
cp $configPath $appPath

cd $appPath
echo "start server"
python3 main.py 2&1>>$modelPath
echo "end" 