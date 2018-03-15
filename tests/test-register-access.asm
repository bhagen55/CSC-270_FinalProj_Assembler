# Test that all 16 registers can be accessed and written to
# The registers from $0 - $15 should hold 1 - 16
addi $0 $0 1
addi $1 $1 2
addi $2 $2 3
addi $3 $3 4
addi $4 $4 5
addi $5 $5 6
addi $6 $6 7
addi $7 $6 1
addi $8 $6 2
addi $9 $6 3
addi $10 $6 4
addi $11 $6 5
addi $12 $6 6
addi $13 $6 7
addi $14 $13 1
addi $15 $13 2
