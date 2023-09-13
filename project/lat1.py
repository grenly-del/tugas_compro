# x = 1
# y = 2
# z = 3
# print("----------------( 1, 2, 3)-----------------")
# print(f"1x1 = {1*x}     2x1={1*y}       3x1={1*z}")
# print(f"1x2 ={2*x}      2x2={2*y}       3x2={2*z}")
# print(f"1x3 ={3*x}      2x3={3*y}       3x3={3*z}")
# print(f"1x4 ={4*x}      2x4={4*y}       3x4={4*z}")
# print(f"1x5 ={5*x}      2x5={5*y}       3x5={5*z}")
# print(f"1x6 ={6*x}      2x6={6*y}       3x6={6*z}")
# print(f"1x7 ={7*x}      2x7={7*y}       3x7={7*z}")
# print(f"1x8 ={8*x}      2x8={8*y}       3x8={8*z}")
# print(f"1x9 ={9*x}      2x9={9*y}       3x9={9*z}")
# print(f"1x10 ={10*x}    2x10={10*y}     3x10={10*z}")
# print("==============================================")


# x = int(input("masukkan angka : "))
# print("----------------( 1, 2, 3)-----------------")
# print(f"{x}x1 ={1*x}")
# print(f"{x}x2 ={2*x}")
# print(f"{x}x3 ={3*x}")
# print(f"{x}x4 ={4*x}")
# print(f"{x}x5 ={5*x}")
# print(f"{x}x6 ={6*x}")
# print(f"{x}x7 ={7*x}")
# print(f"{x}x8 ={8*x}")
# print(f"{x}x9 ={9*x}")
# print(f"{x}x10 ={10*x}")
# print("==============================================")



# print("1"*8)

x = int(input("Masukkan : "))

for i in range(1, 11):
    for j in range(1,x+1):
        result = i*j
        print(f"{j}x{i}={result}", end="\t")
    print("")