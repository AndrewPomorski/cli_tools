#!/bin/bash
# find pid of a process listening on given port and kill it
kill -9 $(lsof -ti tcp:$1)

