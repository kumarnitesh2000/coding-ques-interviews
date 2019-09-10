def print_substring(input,output):
    if len(input)==0:
        print(output)
        return

    print_substring(input[1:],output)
    print_substring(input[1:],output+input[0])


inp="abc"
out=""
print_substring(inp,out)