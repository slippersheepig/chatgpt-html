> **Warning**
> 此分支已失效，除非有旧的官方API泄露或新的官方API发布
# chatgpt-html
### 使用acheong08的官方ChatGPT接口，实现简单HTML网页版在线聊天

> 该版本基于`ChatGPT`开发，想使用OPENAI API KEY的请访问[chatgpt-web](https://github.com/slippersheepig/chatgpt-web)

#### 项目由来及一些说明
- 想在html实现人人可访问的ChatGPT网页应用
- ChatGPT本身支持上下文关联，但个人技术菜鸡，无法在html编写连续对话
- ChatGPT的回复内容比OPENAI API KEY更`自然`，特别是面对复杂表达或场景时，下图为例
![S{_0)XRVDB(3)SKFR$4P7VV](https://user-images.githubusercontent.com/58287293/212858122-1e3c72f5-5f40-4ff8-8e12-3cfb64b3b543.png)

## 部署
### 获取OpenAI API KEY
- 建议参考[此教程](https://blog.csdn.net/hekaiyou/article/details/128303729)获取
### 配置
#### 使用Docker Compose
> 以下文件放同一目录
- 新建`.env`文件，粘贴以下代码并保存
```bash
OPENAI_API_KEY="前面获取到的OpenAI API KEY"
```
- 新建`chat.html`网页文件，粘贴以下代码并保存（UI很丑，建议各自美化）
```html
<!DOCTYPE html>
<html lang="en">

<!--自适应屏幕大小-->
<meta name="viewport" content="width=device-width,initial-scale=1" />

<head>
    <!-- <link rel="shortcut icon" href="" type="image/x-icon" /> -->
    <meta charset="UTF-8">
    <title>ChatGPT</title>
    <style>
      body {
        color: #333;
        background-color: #eee;
      }
    @media (prefers-color-scheme: dark) {
      body {
        background: black;
        color: white;
      }
    }
    </style>
</head>

<body>
    <div align="center">
        <h2>ChatGPT</h2>
        <div>注意：接口返回可能比较慢（服务在国外，并且ChatGPT返回速度也比较慢），提交后需要等待处理完成，请勿重复提交！！！</div>
        <div>~接口返回有长度限制~</div>
        <hr />
        {% if message %} {{ message }} {% endif %}
        <form method="post" onsubmit="submit.disabled=true">
            <textarea style="width:35%;" name="question" placeholder="点击这里输入问题" rows="11" id="form"></textarea>
            <br>
            <input type="submit" style="width:150px;height:50px;background-color:green;font-size:30px" value="提交" id="submit" />
        </form>
        <div id="loading" style="display:none; color:red"><b>后端正在处理，请稍等...</b></div>
        {% if question %}
        <div style="text-align: left"><b>人类:</b>
            <pre id="question">{{ question }}</pre>
        </div>
        <hr />
        <div style="text-align: left"><b>人工智障:</b>
            <pre style="text-align:left; white-space: pre-wrap;" id="res">{{ res }}</pre>
        </div>
        {% endif %}
    </div>
</body>
<script>
    let loading = document.getElementById('loading');
    let form = document.querySelector('form');
    form.addEventListener('submit', () => {
        loading.style.display = 'block';
    });
</script>
</html>
```
- 新建`docker-compose.yml`配置文件，粘贴以下内容并保存
```bash
version: '3'
services:
  chatgpt:
    image: sheepgreen/chatgpt-html:api #如果是arm，请换成chatgpt-html:apiarm
    container_name: htmchat
    volumes:
      - ./.env:/home/appuser/.env
      - ./chat.html:/home/appuser/templates/chat.html
    ports:
      - "9999:80" #80为容器内部端口，9999为外部映射端口，可自行更改
    restart: always
```
- 输入`docker-compose up -d`即启动成功
## 注意事项
- 访问地址为http://ip:port
- 修改`chat.html`文件后，需要docker restart htmchat才能生效
