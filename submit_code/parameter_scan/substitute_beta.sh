#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <Number of flavours> <Beta>"
  exit 1
fi

# Set the arguments
num_flavours=$1
beta=$2

# Multiply beta by 10 and convert it to an integer
multiplied_beta=$(echo "$beta * 10" | bc)
integer_beta=${multiplied_beta%.*}

# Replace values in the test1 script
sed -i "s/--beta [0-9]*\.[0-9]*/--beta $beta/" test1
sed -i "s/_b[0-9]*/_b$integer_beta/" test1
sed -i "s/nf[0-9]*/nf$num_flavours/" test1
sed -i "s/Test_hmc_Sp_Wilson_[0-9]*/Test_hmc_Sp_Wilson_$num_flavours/" test1

# Replace values in the test2 script
sed -i "s/--beta [0-9]*\.[0-9]*/--beta $beta/" test2
sed -i "s/_b[0-9]*/_b$integer_beta/" test2
sed -i "s/nf[0-9]*/nf$num_flavours/" test2
sed -i "s/Test_hmc_Sp_Wilson_[0-9]*/Test_hmc_Sp_Wilson_$num_flavours/" test2

# Replace values in the test3 script
sed -i "s/--beta [0-9]*\.[0-9]*/--beta $beta/" test3
sed -i "s/_b[0-9]*/_b$integer_beta/" test3
sed -i "s/nf[0-9]*/nf$num_flavours/" test3
sed -i "s/Test_hmc_Sp_Wilson_[0-9]*/Test_hmc_Sp_Wilson_$num_flavours/" test3

# Replace values in the test4 script
sed -i "s/--beta [0-9]*\.[0-9]*/--beta $beta/" test4
sed -i "s/_b[0-9]*/_b$integer_beta/" test4
sed -i "s/nf[0-9]*/nf$num_flavours/" test4
sed -i "s/Test_hmc_Sp_Wilson_[0-9]*/Test_hmc_Sp_Wilson_$num_flavours/" test4

