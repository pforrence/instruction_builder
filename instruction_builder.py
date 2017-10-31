r_dict = {"add" : "000000", "addu" : "000000", "sub" : "000000", "subu" : "000000", 
        "and" : "000000", "or" : "000000", "xor" : "000000", "nor" : "000000", 
        "sll" : "000000", "srl" : "000000", "sra" : "000000", "sllv" : "000000", 
        "srlv" : "000000", "srav" : "000000", "slt" : "000000", "sltu" : "000000", 
        "clo" : "011100", "clz" : "011100"}
i_dict = {"addi" : "001000", "addiu" : "001001", "andi" : "001100", "ori" : "001101", 
        "xori" : "001110", "slti" : "001010", "sltiu" : "001011", "lb" : "100000", 
        "lbu" : "100100", "lh" : "100001", "lhu" : "100101", "lw" : "100011", 
        "lui": "001111", "sb" : "101000", "sh" : "101001", "sw" : "101011",
        "beq" : "000100", "bne" : "000101", "bltz": "000001", "bgez" : "000001", 
        "bltzal" : "000001", "bgezal" : "000001", "blez" : "000110", "bgtz" : "000111"}
j_dict = {"j" : "000010", "jal" : "000011", "jr" : "000000", "jalr": "000000"}


funct_dict = {"add" : "100000", "addu" : "100001", "sub" : "100010", "subu" : "100011", 
        "and" : "100100", "or" : "100101", "xor" : "100110", "nor" : "100111", 
        "sll" : "000000", "srl" : "000010", "sra" : "000011", "sllv" : "000100", 
        "srlv" : "000110", "srav" : "000111", "slt" : "101010", "sltu" : "101011", 
        "clo" : "100001", "clz" : "100000"}
extention = '.do'
def printable_bin(string):
    if int(string) <= 31 and int(string) > -1:
        return "{0:05b}".format(int(string))
    print("out of bounds")
    return -1

def printable_imm(string):
    if int(string) <= 65535 and int(string) > -1:
        return "{0:016b}".format(int(string))

    print("out of bounds")
    return -1

def printable_index(string):
    if int(string) <= 67108863 and int(string) > -1:
        return "{0:026b}".format(int(string))
    print("out of bounds")
    return -1



def r_type(op, instr):
    rs = printable_bin(input('Enter your rs (0-31 decimal): '))
    while rs is -1:
        rs = printable_bin(input('Enter your rs (0-31 decimal): '))
    print(rs)

    rt = printable_bin(input('Enter your rt (0-31 decimal): '))
    while rt is -1:
        rt = printable_bin(input('Enter your rt (0-31 decimal): '))
    print(rt)

    rd = printable_bin(input('Enter your rd (0-31 decimal): '))
    while rd is -1:
        rd = printable_bin(input('Enter your rd (0-31 decimal): '))
    print(rd)

    shamt = printable_bin(input('Enter your shamt (0-31 decimal): '))
    while shamt is -1:
        shamt = printable_bin(input('Enter your shamt (0-31 decimal): '))
    print(shamt)    
    print("funct: ")
    print(funct_dict[instr])
    instr = op+rs+rt+rd+shamt+funct_dict[instr]
    print(instr)
    return instr

def i_type(op):
    rs = printable_bin(input('Enter your rs (0-31 decimal): '))
    while rs is -1:
        rs = printable_bin(input('Enter your rs (0-31 decimal): '))
    print(rs)

    rt = printable_bin(input('Enter your rt (0-31 decimal): '))
    while rt is -1:
        rt = printable_bin(input('Enter your rt (0-31 decimal): '))
    print(rt)

    imm = printable_imm(input('Enter your immediate (0-65535 decimal): '))
    while imm is -1:
        imm = printable_imm(input('Enter your immediate (0-65535 decimal): '))
    print(imm)    

    instr = op+rs+rt+imm
    print(instr)
    return instr

def j_type(op):
    index = printable_index(input('Enter your instr_index (0-67108863 decimal): '))
    print(index)    

    instr = op+index
    print(instr)
    return instr

def main():
    instructions = []
    while True:
        instruction_name = input('Type \'break\' to break \nEnter your instruction name (sub, addi, j): ')
        if instruction_name in r_dict:
            print("r: "+r_dict[instruction_name])
            instructions.append(r_type(r_dict[instruction_name], instruction_name))
        elif instruction_name in i_dict:
            print("i: "+i_dict[instruction_name])
            instructions.append(i_type(i_dict[instruction_name]))
        elif instruction_name in j_dict:
            print("j: "+j_dict[instruction_name])
            instructions.append(j_type(j_dict[instruction_name]))
        elif instruction_name == "break":
        	break
        else:
            print("I don't recognize this instruction")
    print("\n\nHERE ARE YOUR INSTRUCTIONS:")
    for i in instructions:
        print(i)
    filename = input('Filename: ')
    if extention not in filename:
        filename = filename + extention

    yes = input('Append or write (A/w): ')
    if yes is not 'w' and yes is not 'a':
        yes = 'a'

    with open(filename, yes) as f:
        f.write("restart -f\n")
        f.write("do test/basic.do \n")
        f.write("force -freeze clock 0 0, 1 {50 ns} -r 100\n")
        for i in instructions:
            f.write("force INST_MemoryDataIn \""+i+"\"\nrun 100\n")

main()

# "add" : "000000", 
# "addu" : "000000", 
# "addi" : 001000, 
# "addiu" : 001001, 
# "sub" : "000000", 
# "subu" : "000000",
# "and" : "000000", 
# "andi" : 001100, 
# "or" : "000000", 
# "ori" : 001101, 
# "xor" : "000000", 
# "xori" : 001110, 
# "nor" : "000000", 
# "sll" : "000000", 
# "srl" : "000000", 
# "sra" : "000000", 
# "sllv" : "000000", 
# "srlv" : "000000", 
# "srav" : "000000", 
# "slt" : "000000", 
# "sltu" : "000000", 
# "slti" : 001010, 
# "sltiu" : 001011
# "clo" : 011100, 
# "clz" : 011100, 
# "lb" : 100000, 
# "lbu" : 100100, 
# "lh" : 100001, 
# "lhu" : 100101, 
# "lw" : 100011, 
# "lui": 001111, 
# "sb" : 101000, 
# "sh" : 101001, 
# "sw" : 101011,
# "beq" : 000100, 
# "bne" : 000101, 
# "bltz": 000001 
# "bgez" : 000001, 
# "bltzal" : 000001, 
# "bgezal" : 000001, 
# "blez" : 000110,
# "bgtz" : 000111, 
# "j" : 000010, 
# "jal" : 000011, 
# "jr" : "000000", 
# "jalr": "000000"
