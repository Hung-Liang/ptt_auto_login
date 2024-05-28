# PTT auto login

## Introduction

- 這是一個自動登入PTT的程式，讓你可以每天自動登入PTT去累積登入天數。
- 這個程式是使用python寫的，並且使用PyPtt套件來登入PTT。

## How to use

- 這個程式是使用docker來執行的，所以你需要先安裝docker。
- 你可以使用下面的指令來建立docker image，並且執行docker container。

```bash
    docker build --no-cache -t ptt_auto_login .
    sudo docker run --restart always -d ptt_auto_login
```

- 這個程式會在每天的早上八點自動執行，並且登入PTT。
