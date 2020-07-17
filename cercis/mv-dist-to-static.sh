#!/bin/bash

pushd .

cd public/dist/js
find . -regex '.*/chunk.+\.js' -exec mv {} vendor.js \;
find . -regex '.*/app.+\.js' -exec mv {} app.js \;

cd ../css
find . -regex '.*/app.+\.css' -exec mv {} app.css \;

popd

rm -rf static/js/vendor.js
rm -rf static/js/app.js
rm -rf static/css/app.css

cp -r public/dist/js static
cp -r public/dist/css static