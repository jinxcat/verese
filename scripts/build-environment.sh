#!/bin/bash
#
# invoke as
# ~$ bash ./scripts/build-environment.sh

# install django
pip -E env install django

# activate environment
source env/bin/activate

# install the rest
pip install south
# pip install piston
# pip install tastypie