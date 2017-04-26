#!/bin/bash

for i in {1..100000}
do
j=$(( $j + $i ))
done
echo $j
