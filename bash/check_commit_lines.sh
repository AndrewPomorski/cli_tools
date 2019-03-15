#!/usr/bin/env bash
git log --author="$1" --since="1 day ago" --format= --numstat | awk '{s+=$1; s+=$2} END {print s}'

