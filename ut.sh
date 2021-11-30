#!/bin/bash

function upload_codecov_report {
  # upload_codecov_report <dir> <flag>
  cd "$1" || return 126
  wget --no-check-certificate https://codecov.io/bash -O codecov.sh
  pwd
  bash codecov.sh -cF "$2"
}


function run_java {
  mvn test -B || return 126
  cd ../../
  upload_codecov_report java java
}



function run_python {
  #env
  export PYTHONPATH=$PYTHONPATH:`pwd`/python
  echo $PYTHONPATH 
  # install
  pip install coverage
  pip install alibabacloud-tea
  cd ../
  upload_codecov_report python python
}

function contains {
  local value=$2
  for i in $1
  do
    if [ "$i" == "$value" ]; then
      echo "y"
      return 0
    fi
  done
  echo "n"
  return 1
}

lang=$1

if [ "$lang" == "java" ]
then
  echo "run java"
  run_java
elif [ "$lang" == "python" ] 
then
  echo "run python"
  run_python
fi

exit $?