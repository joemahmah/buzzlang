from collections import deque

def readFile():
	filename = raw_input("File: ")
	file = open(filename)

	file_contents = deque()

	for line in file:
		file_contents.append(line)

	return file_contents

def replaceContents(file):
	file_new = deque()

	for line in file:
		line = line.replace("#in case of","#if")
		line = line.replace("#however, in case of","#elif")
		line = line.replace("#otherwise","#else")
		line = line.replace("#that's all I have to say about that.","#endif")
		line = line.replace("#if there exists","#ifdef")
		line = line.replace("#if there doesn't exist","#ifndef")
		line = line.replace("#prescribe","#define")
		line = line.replace("#unprescribe","#undef")
		line = line.replace("#I want","#include")
		line = line.replace("clambake","asm")
		line = line.replace("what is","auto")
		line = line.replace("referendum","bool")
		line = line.replace("renounce this","break")
		line = line.replace("conditionally for","case")
		line = line.replace("mission failed","catch")
#		line = line.replace("","char")
		line = line.replace("corporation","class")
		line = line.replace("immutable","const")
		line = line.replace("recommence","continue")
		line = line.replace("and it shall be","decltype")
		line = line.replace("outside the box","default")
		line = line.replace("expunge","delete")
		line = line.replace("transliterate","do")
		line = line.replace("real number","double")
		line = line.replace("otherwise","else")
		line = line.replace("embodiment","enum")
		line = line.replace("drop the mic","exit(0)")
#		line = line.replace("","explicit")
		line = line.replace("ersatz","false")
		line = line.replace("almost a real number","float")
		line = line.replace("in consideration of","for")
		line = line.replace("associate","friend")
		line = line.replace("teleport to","goto")
		line = line.replace("in the event that","if")
		line = line.replace("not so big perfect number","short")
		line = line.replace("big perfect number","long")
		line = line.replace("perfect number","int")
		line = line.replace("chmod 777","mutable")
		line = line.replace("precedent","namespace")
		line = line.replace("allocating resources towards","new")
		line = line.replace("unsanctioned whereabouts","nullptr")
#		line = line.replace("","operator")
		line = line.replace("confidential","private")
		line = line.replace("safeguarded","protected")
		line = line.replace("common core","public")
		line = line.replace("deport","return")
		line = line.replace("optimistic","signed")
#		line = line.replace("","sizeof")
		line = line.replace("godly","static")
		line = line.replace("shareholder","struct")
		line = line.replace("wave pick","switch")
		line = line.replace("blueprint","template")
		line = line.replace("the aforementioned","this")
		line = line.replace("mission abort","throw")
		line = line.replace("kosher","true")
		line = line.replace("mission critical","try")
		line = line.replace("prescribe","typedef")
		line = line.replace("neutral","unsigned")
		line = line.replace("Appropriating","using")
		line = line.replace("computer generated","virtual")
		line = line.replace("unsanctioned","void")
		line = line.replace("effervescent","volatile")
		line = line.replace("throughout the epoch during which","while")

		line = line.replace("Let there be light.","#include <iostream>\n#include <string>")
		line = line.replace("And that's all I have to say about that.","return 0;\n}")
		line = line.replace("Let us begin.","int main(int argc, char** argv){")
		line = line.replace("Verbalize","cout <<")
		line = line.replace("Hearken","cin >>")
		line = line.replace("and also verbalize","<<")
		line = line.replace("and also hearken",">>")
		line = line.replace("orthodox.","std;")
		line = line.replace("and read next line."," << endl;")

		file_new.append(line)

	return file_new

file = readFile()

output_filename = raw_input("Output to: ") + ".cpp"
output_file = open(output_filename, "w")

file = replaceContents(file)

for line in file:
	output_file.write(line)
