#!/usr/bin/env bash

set -e


# Get the absolute path of the directory containing this script
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Get the absolute path of the root directory of the repository
ROOTDIR="$(git -C "$SCRIPTDIR" rev-parse --show-toplevel)"

set -x

# Generate the AUTHORS file in the root directory of the repository
git -C "$ROOTDIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf > "${ROOTDIR}/AUTHORS"

# Display a message indicating that the AUTHORS file has been generated
echo "AUTHORS file generated successfully at ${ROOTDIR}/AUTHORS"
