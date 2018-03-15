addi $1 $0 4
addi $2 $0 5
slt $3 $1 $2 # $3 should be 1 since $1 < $2
sgt $4 $1 $2 # $4 should be 0
addi $1 $0 5
addi $2 $0 4
slt $5 $1 $2 # $5 should be 0
sgt $6 $1 $2 # $6 should be 1
