# generate multiple test cases
import os
import subprocess
import shutil

path = {
    "code_file": "./code.cpp",
    "testcases": "./Test Cases",
    "testcase_file": "./testcase.cpp",
    "validator_file": "./validator.cpp",
    "in_file": "./in.txt",
}

def delete_testcase():
    delete = int(input(f"Want to delete \"{path['testcases']}\" folder? (1/0) : "))
    if(delete == 1):
        if(os.path.exists(path['testcases'])):
            shutil.rmtree(path['testcases'])
        os.mkdir(path['testcases'])
        os.mkdir(path['testcases'] + "/input")
        os.mkdir(path['testcases'] + "/output")
        return 0
    elif(delete == 0):
        offset = len(os.listdir(path['testcases'] + "/input"))
        return offset
    else:
        print("exit ..")
        exit()

def run(cmd, std_input = None):
    return subprocess.run(cmd, input = std_input, capture_output = True, shell = True, text = True, check = True)

def compile_files():
    code_file = path['code_file']
    print(f"Compiling {code_file}")
    cmd = f"g++ -std=c++17 {code_file} -o code.exe"
    run(cmd)

    testcase_file = path['testcase_file']
    print(f"Compiling {testcase_file}")
    cmd = f"g++ -std=c++17 {testcase_file} -o testcase.exe"
    run(cmd)

    validator_file = path['validator_file']
    print(f"Compiling {validator_file}")
    cmd = f"g++ -std=c++17 {validator_file} -o validator.exe"
    run(cmd)

    print("Compilation done")

def process(offset):
    t = int(input("\nNumber of test cases : "))
    if(t >= 1):
        for i in range(t):
            print("\nCase #", i, sep = '')

            input_file_path = path['testcases'] + "/input/input{0:0=2d}.txt".format(i + offset)
            output_file_path = path['testcases'] + "/output/output{0:0=2d}.txt".format(i + offset)

            #create file
            print("creating files")
            open(input_file_path, 'x')
            open(output_file_path, 'x')

            try:
                #generate testcase
                print("generating testcase")
                cmd = f"testcase.exe > \"{input_file_path}\""
                run(cmd)

                # validate testcase
                print("validating testcase")
                cmd = f"validator.exe < \"{input_file_path}\""
                run(cmd)

                # run cpp file to generate output
                print("running code")
                cmd = f"code.exe < \"{input_file_path}\" > \"{output_file_path}\""
                run(cmd)

                print("SUCCESS", input_file_path)
                print("SUCCESS", output_file_path)

            except Exception as e:
                print("\nsomething went wrong :(")
                print("check \"in.txt\" file\n")

                with open(input_file_path, "r") as f1, open(path['in_file'], "w") as f2:
                    f2.write(f1.read())

                print(e, "\n")
                
                print("deleting input & outut files")
                os.remove(input_file_path)
                os.remove(output_file_path)
                exit()

            except KeyboardInterrupt:
                print("Keyboard Interrupt.")
                exit()

if __name__ == "__main__":
    offset = delete_testcase()
    compile_files()
    process(offset)