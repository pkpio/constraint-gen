X_INDEX = 10
Y_START = 157
LENGTH = 128

BEL_INST0 = "D6LUT"
BEL_INST1 = "A6LUT" 

# Sample instance is sh/mp/picn/puf1/sarray[0]/pdl_top/LUT6_inst_1
INST_P1 = "sh/mp/picn/puf1/sarray["
INST_P2 = "]/pdl_top/LUT6_inst_"

f = open('constraints.txt','w')

for i in range(0, LENGTH):
	const = "INST \"" + INST_P1 + str(i) + INST_P2 + "0\" BEL = " + BEL_INST0 + ";\n"
	const += "INST \"" + INST_P1 + str(i) + INST_P2 + "0\" LOC = SLICE_X" + str(X_INDEX) + "Y" + str(Y_START-i) + ";\n"
	const += "INST \"" + INST_P1 + str(i) + INST_P2 + "0\" BEL = " + BEL_INST0 + ";\n"
	const += "INST \"" + INST_P1 + str(i) + INST_P2 + "0\" LOC = SLICE_X" + str(X_INDEX) + "Y" + str(Y_START-i) + ";\n\n"
	
	f.write(const)


f.close() 
