# FastAPI サンプルおよび外部アクセス手順

FastAPI の最小サンプルコードと、ローカルおよびインターネットからアクセス可能にする手順。

---

必要環境:
- Python 3.10 以上
- pip が利用可能であること

インストール:

    pip install fastapi uvicorn[standard]



サーバ起動:

    uvicorn main:app --host 0.0.0.0 --port 8000

- --host 0.0.0.0 を指定すると外部からアクセス可能になる。

---

ローカルネットワークからのアクセス:

- サーバ端末の LAN 内 IP を確認して以下にアクセスする:

    http://<LAN内IP>:8000/

例:

    http://192.168.1.10:8000/

---

インターネット（グローバル）からアクセスする手順:

グローバル IP または DDNS を利用する。

OS のファイアウォール設定（例: Linux / ufw）:

    sudo ufw allow 8000/tcp

外部確認:

    http://<グローバルIPまたはDDNS>:8000/



参考:
FastAPI 公式ドキュメント  
https://fastapi.tiangolo.com/
