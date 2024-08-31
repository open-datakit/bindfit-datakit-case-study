#! /usr/bin/env bash
# Build bindfit container first with containers/build.sh script
docker run -it -v ${PWD}:/usr/src/app/datapackage -e ALGORITHM=bindfit -e ARGUMENT_SPACE=default ods/bindfit
