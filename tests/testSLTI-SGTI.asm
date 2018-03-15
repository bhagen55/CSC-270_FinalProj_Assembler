# Test immediate version of slt and sgt
# At the end,
# $3/$5/$9 should be 1
# $2/$4/$6/$7/$8 should be 0
addi $1 $0 4
addi $2 $0 3
addi $3 $0 3
addi $4 $0 3
addi $5 $0 3
addi $6 $0 3
addi $7 $0 3
addi $8 $0 3
addi $9 $0 3
slti $2 $1 3 # $2 should be 0
slti $3 $1 5 # $3 should be 1
slti $4 $1 4 # $4 should be 0
sgti $5 $1 3 # $5 should be 1
sgti $6 $1 5 # $6 should be 0
sgti $7 $1 4 # $7 should be 0
slti $8 $1 -4 # $8 should be 0
sgti $9 $1 -4 # $9 should be 1
