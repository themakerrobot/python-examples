# install

pip3
<pre>
<code>
fastapi==0.68.0
uvicorn==0.15.0
python-multipart==0.0.5
pyyaml
soundfile
tensorflow
tensorflowtts
pororo
pydub
</code>
</pre>

+ wav2letter install -> wav2letter/bindings/python -> pip3 install -e .
+ pip3 install git+https://github.com/repodiac/german_transliterate


+ proxy
 - stg-neapi.circul.us 192.168.2.154 58821
 - ops-neapi.circul.us 192.168.3.254 59821


STG
<pre><code>
server {
  listen 58821;
  client_max_body_size 20M;

  location /v1/stt {
    proxy_pass http://127.0.0.1:10001/stt;
  }
  location /v1/tts {
    proxy_pass http://127.0.0.1:10002/tts;
  }

  location /stt {
    proxy_pass http://127.0.0.1:10001/stt;
  }
  location /tts {
    proxy_pass http://127.0.0.1:10002/tts;
  }
}

OPS
server {
  listen 59821;
  client_max_body_size 20M;

  location /v1/stt {
    proxy_pass http://127.0.0.1:10001/stt;
  }
  location /v1/tts {
    proxy_pass http://127.0.0.1:10002/tts;
  }

  location /stt {
    proxy_pass http://127.0.0.1:10001/stt;
  }
  location /tts {
    proxy_pass http://127.0.0.1:10002/tts;
  }
}
</code></pre>
