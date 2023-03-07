> **Warning** 为维持docker镜像的小体积，本分支不再更新revChatGPT版本，除非作者对依赖做了调整（并没有怪作者的意思，相反，很感谢他做的贡献，致敬）
# Update
 - 2023.3.7 小改代码，实现多用户独立会话互不干扰，并且不影响每个用户的连续对话（临时性方案，等作者重写核心代码）
 - 2023.3.3 现支持按回车发送问题请求，按shift+回车可换行输入文本
+ 2023.2.28 关于OPENAI允许问题的最大长度
  + 根据OPENAI官方[问答](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)"Depending on the [model](https://platform.openai.com/docs/models/gpt-3) used, requests can use up to 4097 tokens shared between prompt and completion. If your prompt is 4000 tokens, your completion can be 97 tokens at most"，虽然没有明确指出ChatGPT模型是否也适用，但结合谷歌搜索的结果，应该一样。问题和回答加起来的总长度无法超过4097个token，如果你不清楚自己问题的长度，可以使用[官方计数器](https://platform.openai.com/tokenizer)
 - 2023.2.20 `支持markdown语法`
 - 2023.2.19 `重构关键代码，内置本人使用的UI，支持查看连续对话记录`
# chatgpt-html
### 使用[acheong08](https://github.com/acheong08/ChatGPT)的非官方ChatGPT接口，实现简单HTML网页版在线聊天

> 该版本基于`ChatGPT`网页端代理开发（免费），想使用ChatGPT API KEY（付费）的请访问[chatgpt-web](https://github.com/slippersheepig/chatgpt-web)

#### 项目由来及一些说明
- 想在html实现人人可访问的ChatGPT网页应用
- `通过连接代理服务器响应ChatGPT请求，客户端无需模拟浏览器登录，代理服务端建议自行搭建（作者未公开方法，但在作者github可以找到，出于对作者的尊敬此处也不公开，请自行查找）`
- 如更改了项目代码，建议自行使用Dockerfile构建镜像

## 部署
### 获取OpenAI账号（即邮箱）及密码（`请使用普通方式注册，不支持谷歌或者微软快捷登录`）
- 点击注册[OpenAI](https://platform.openai.com/)
### 配置
#### 使用Docker Compose
> 以下所有文件放同一目录
- 新建`config.json`文件，粘贴以下代码并保存
```bash
{
        "__comment01__": "邮箱、session_token和access_token三选一",
        "__comment02__": "邮箱认证",
        "email": "",
        "password": "",
        "__comment03__": "session_token认证",
        "session_token": "",
        "__comment04__": "access_token认证",
        "access_token": "",
        
        "__comment05__": "以下为选填字段",
        "__comment06__": "通过代理连接代理端（作者服务器被墙过，代理好像只能用无密码认证的socks5或者http，请自行测试）",
        "proxy": "",
        "__comment07__": "使用付费openai账号（官方称速度更快，无频率限制，将false改为true）",
        "paid": false
}
```
 - session_token获取方法（随时过期）
1. Go to https://chat.openai.com/chat and open the developer tools by `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field.
 - access_token获取方法（据说可以持续2周不过期）

登录ChatGPT官方网页版后再打开https://chat.openai.com/api/auth/session 

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
- 修改`chat.html`文件后，需要docker restart htmchat才能生效
