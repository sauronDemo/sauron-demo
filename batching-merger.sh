#!/bin/bash -e

if [[ -e batch ]]; then
  cat batch | xargs -I% git merge %
fi
