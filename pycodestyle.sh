#!/usr/bin/bash

pycodestyle *.py ; cd models ; pycodestyle *.py ; cd engine ;
pycodestyle *.py ; cd ../../tests ; pycodestyle *.py ;
cd test_models ; pycodestyle *.py ; cd test_engine ;
pycodestyle *.py ; cd ../../../

echo "Pycode style was ran in:"
echo "./"
echo "./models/"
echo "./models/engine/"
echo "./tests/"
echo "./tests/test_models/"
echo "./tests/test_models/test_engine/"
