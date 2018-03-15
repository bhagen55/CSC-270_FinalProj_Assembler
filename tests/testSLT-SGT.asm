# Test the SLT and SGT operations of the processor
# At the end, $3/$6 should be 1, $4/$5 should be 0
# If any of the above registers are 3, they were not modified
addi $1 $0 4
addi $2 $0 5
addi $3 $0 3 # Set $3-$6 to 3 to make errors with setting to 0 noticeable
addi $4 $0 3
addi $5 $0 3
addi $6 $0 3
addi $7 $0 3
addi $8 $0 3
slt $3 $1 $2 # $3 should be 1 since $1 < $2
sgt $4 $1 $2 # $4 should be 0
addi $1 $0 5
addi $2 $0 4
slt $5 $1 $2 # $5 should be 0
sgt $6 $1 $2 # $6 should be 1
addi $1 $0 -5
addi $2 $0 0
slt $7 $1 $2 # $7 should be 1
sgt $8 $1 $2 # $8 should be 0
