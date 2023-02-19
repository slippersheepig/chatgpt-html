2023.2.19 `重构关键代码，内置本人使用的UI，支持查看连续对话记录`
> 使用acheong08最新的代理接口，大幅减轻服务器负载，客户端可在国内搭建（如需境外本地搭建，请切换main分支）
# chatgpt-html
### 使用[acheong08](https://github.com/acheong08/ChatGPT)的非官方ChatGPT接口，实现简单HTML网页版在线聊天

> 该版本基于`ChatGPT`开发，想使用OPENAI API KEY的请访问[chatgpt-web](https://github.com/slippersheepig/chatgpt-web)

#### 项目由来及一些说明
- 想在html实现人人可访问的ChatGPT网页应用
- `通过连接代理服务器响应ChatGPT请求，客户端无需模拟浏览器登录，代理服务端建议自行搭建（作者未公开方法，但在作者github可以找到，出于对作者的尊敬此处也不公开，请自行查找）`
- 如更改了项目代码，建议自行使用Dockerfile构建镜像
- ChatGPT的回复内容比OPENAI API KEY更`自然`，特别是面对复杂表达或场景时，下图为例
![S{_0)XRVDB(3)SKFR$4P7VV](https://user-images.githubusercontent.com/58287293/212858122-1e3c72f5-5f40-4ff8-8e12-3cfb64b3b543.png)

## 部署
### 获取OpenAI账号（即邮箱）及密码（`请使用普通方式注册，不要谷歌或者微软快捷登录`）
- 点击注册[OpenAI](https://platform.openai.com/)
### 配置
#### 使用Docker Compose
> 以下所有文件放同一目录
- 新建`config.json`文件，粘贴以下代码并保存
```bash
{
        "email": "填写你的OpenAI账号（即邮箱）",
        "password": "填写你的OpenAI密码"
}
```
- 新建`docker-compose.yml`配置文件，粘贴以下内容并保存
```bash
services:
  chatgpt:
    image: sheepgreen/chatgpt-html:proxy #如果是arm架构，请换成chatgpt-html:proxyarm
    container_name: htmchat
#    environment:
#      - CHATGPT_BASE_URL=你的代理服务端地址（不填默认使用作者服务器，目前偶尔会不可用）
    volumes:
      - ./config.json:/chatgpt-html/config.json
#      - ./chat.html:/chatgpt-html/templates/chat.html #默认内置我的UI，如需替换自用网页请取消注释
    ports:
      - "9999:8088" #8088为容器内端口，不可更换；9999为外部端口，可自行更换
    restart: always
```
- 输入`docker-compose up -d`即启动成功
## 注意事项
- 访问地址为http://ip:port
