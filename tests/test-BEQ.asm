# Test the branch if equal to command
# There should be no -1s in any register
addi $1 $0 7
addi $2 $0 -7
addi $3 $0 7
addi $4 $0 -7
beq $1 $3 1
addi $5 $0 -1
beq $1 $2 1
addi $6 $0 1
beq $2 $4 1
addi $7 $0 -1
addi $8 $0 1
