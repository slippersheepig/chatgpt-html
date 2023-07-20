# chatgpt-html
### 使用[acheong08](https://github.com/acheong08/ChatGPT)对接官方ChatGPT接口，实现简单HTML网页版在线聊天
> 该版本基于`ChatGPT`网页端代理开发（免费），想使用ChatGPT API KEY（付费）的请访问[chatgpt-web](https://github.com/slippersheepig/chatgpt-web)
### 注意
> 使用该项目的前提是你的服务器IP没有被BAN，由于我自己的服务器IP已BAN，无法测试项目是否可用，请自行尝试
## 特性
- 文件结构简单，主要面向小白用户
- 功能不多，但核心的连续对话、多用户会话隔离、markdown格式输出都具备
## 部署
#### 使用Docker Compose
> 以下所有文件放同一目录
- 新建`config.json`文件，粘贴以下代码并保存
```bash
{
        "__comment01__": "邮箱、session_token和access_token三选一",
        "__comment02__": "邮箱认证（暂仅支持普通方式注册的账号，不支持谷歌或微软快捷登录）",
        "email": "",
        "password": "",
        "__comment03__": "session_token认证（不受账号注册方式影响）",
        "session_token": "",
        "__comment04__": "access_token认证（不受账号注册方式影响）",
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
    image: sheepgreen/chatgpt-html
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
## 其他相关
- [ChatGPT电报机器人](https://github.com/slippersheepig/chatgpt-telegram-bot)，[ChatGPT企业微信应用机器人](https://github.com/slippersheepig/chatgpt-bizwechat-bot)，[ChatGPT的QQ频道机器人DOCKER版](https://github.com/slippersheepig/QQChannelChatGPT)，[微软BING电报机器人DOCKER版](https://github.com/slippersheepig/BingChatBot)，[谷歌BARD网页版](https://github.com/slippersheepig/bard-web)，[谷歌BARD电报机器人](https://github.com/slippersheepig/bard-telegram-bot)
- 出于玩玩bing的chatgpt心态，按[waylaidwanderer](https://github.com/waylaidwanderer/PandoraAI)搞了一套[测试站](https://ai.sheepig.top)（需要先点击聊天框左边的图标切换模型，默认模型是API，我的KEY没额度了），`Bing`就是GPT-4，`Sydney`是“破解”过的Bing（没有每轮对话最多15次和每天对话最多150次的限制，但是智商差一点）。另外此项目代码也有bug需要完善（如果你去体验会发现的），不做详细介绍。
![RIVG68}0DCNFD)8MH@OO%W2](https://user-images.githubusercontent.com/58287293/225894449-34e4fde8-8add-4674-8231-c78c6025a913.png)
![~@M18}0M{LXG6$`5{ZDG{XU](https://user-images.githubusercontent.com/58287293/225894846-a5cb608a-3f1f-4740-ac86-c3601b1a3ad5.png)
- 基于[pandora](https://github.com/pengzhile/pandora)制作了官方OPENAI CHATGPT[高仿站](https://v.sheepig.top)
