# PTT auto login

## Introduction

- 這是一個自動登入PTT的程式，讓你可以每天自動登入PTT去累積登入天數。
- 這個程式是使用python寫的，並且使用PyPtt套件來登入PTT。

## How to use

- 你需要先把專案clone到你的電腦上。
- 然後將.env.example檔案複製一份，並且命名為.env。
- 你需要在.env檔案中填入你的PTT帳號和密碼。還有telegram的bot token和chat id。
- 這個程式是使用docker來執行的，所以你需要先安裝docker。
- 你可以使用下面的指令來建立docker image，並且執行docker container。

```bash
    docker build --no-cache -t ptt_auto_login .
    sudo docker run --restart always -d ptt_auto_login
```

- 請在專案的根目錄下執行上面的指令。
- 這個程式會在每天的早上八點自動執行，並且登入PTT。
