#!/usr/bin/env bash

set -e

# Get the absolute path of the root directory of the repository
ROOTDIR="/home/flames/alx/AirBnB_clone"    # Could be dynamic :(

set -x

# Navigate to the root directory of the repository
cd "$ROOTDIR" || exit

# Generate the AUTHORS file in the root directory of the repository
git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf > AUTHORS

# Display a message indicating that the AUTHORS file has been generated
echo "AUTHORS file generated successfully at ${ROOTDIR}/AUTHORS"
