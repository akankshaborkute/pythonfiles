from calulator import squre

# def main():
#     test_squre()

def test_squre():
    assert squre(2)==4
    assert squre(3)==9
    assert squre(-2)==4
    assert squre(-3)==4
    assert squre(0)==0

  
#     # if squre(4)!=16:
#     #     print("4 squred was not 16")
#     # if squre(2)!=4:
#     #     print("2 squre is not 4")        
#     # if squre(3)!=9:
#     #     print("3 squred was not 9")
#     try:
#         assert squre(2)==4
#     except AssertionError:    
#         print("2 squred was not 4")
#     try:
#         assert squre(4)==16
#     except AssertionError:
#         print("4 squred was not 16")
#     try:
#         assert squre(-2)==4
#     except AssertionError:
#         print("-2 squred was not 4")
#     try:
#         assert squre(-3)==9
#     except AssertionError:
#         print("-3 squred was not 9")    
#     try:
#         assert squre(0)==0
#     except AssertionError:
#         print("0 squred was not 0")  

# if __name__=="__main__":
#     main()