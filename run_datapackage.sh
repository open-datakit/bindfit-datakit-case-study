#! /usr/bin/env bash
# Build bindfit container first with containers/build.sh script
docker run -it -v ${PWD}:/usr/src/app/datapackage -e CONFIGURATION=bindfit.default ods/bindfit
