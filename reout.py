# run all the testcase and update output
import os
import subprocess

cpp_file = "./code.cpp"
testcase_file = "./testcase.cpp"
validator_file = "./validator.cpp"
folder_path = "./Test Cases"
in_file = "./in.txt"

def run(cmd, std_input = None):
    return subprocess.run(cmd, input = std_input, capture_output = True, shell = True, text = True, check = True)

# compile testcase and source file
print(f"Compiling {cpp_file}")
cmd = f"g++ -std=c++17 {cpp_file} -o code.exe"
run(cmd)

print(f"Compiling {testcase_file}")
cmd = f"g++ -std=c++17 {testcase_file} -o testcase.exe"
run(cmd)

print(f"Compiling {validator_file}")
cmd = f"g++ -std=c++17 {validator_file} -o validator.exe"
run(cmd)

print("Compilation done\n")

tc = len(os.listdir(folder_path + "/input"))
print("Total testcases:", tc)

ok = int(input("is that ok? (0/1): "))
if(ok != 1 and ok != 0):
    exit(0)

for i in range(tc):
    print("\nCase #", i, sep = '')

    input_file_path = folder_path + "/input/input{0:0=2d}.txt".format(i)
    output_file_path = folder_path + "/output/output{0:0=2d}.txt".format(i)

    try:
        # validate testcase
        print("validating testcase")
        cmd = f"validator.exe < \"{input_file_path}\""
        run(cmd)

        # run cpp file to generate output
        print("running code")
        cmd = f"code.exe < \"{input_file_path}\" > \"{output_file_path}\""
        run(cmd)

        # print("Updated", input_file_path)
        print("Updated", output_file_path)

    except Exception as e:
        print("\nsomething went wrong :(")
        print(e)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        exit()