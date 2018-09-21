#!/bin/bash

# Display useful information about a system for debugging issues
echo 'System information'

echo -e '\nNode version'
node --version

echo -e '\nGlobal NPM packages'
npm list -g --depth=0
