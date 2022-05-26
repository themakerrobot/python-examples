#!/bin/bash

# /etc/crontab
# * * * * * circulus cd /home/circulus/service/ai-voice && ./check_voice.sh >> /home/circulus/log/doctor_voice.log

function check_app () {
  filename=$1_server.py
  chk_ps=`pgrep -lf $filename | wc -l`

  if [ ${chk_ps} -lt 1 ]; then
    echo "[`date '+%Y-%m-%d %H:%M:%S'`]: $1 restart"
    #export PY_ENV=DEV|STG|OPS
    export PY_ENV=$2
    nohup python3 $filename &
  fi
}

# DEV|STG|OPS
#source /home/circulus/VENV/vapi-20210310/bin/activate
#export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64:/usr/local/cuda-10.2/lib64
source /home/circulus/VENV/ne-20210923/bin/activate
mode=OPS
check_app stt $mode
check_app tts $mode
