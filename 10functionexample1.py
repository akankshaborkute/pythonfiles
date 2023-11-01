from urllib.request import urlopen
def main():
    fetch_world()

# def squre(x):
#     return x*x
# a=squre(5)
# print(a)

# def even_odd(x):
#     if x %2==0:
#         print("even")
#         return
#     print("odd")    

# w=even_odd(16)
# print(w)    

# def nth_root(radicand,n):
#     return radicand**(1/n)



# def ordinal_suffix(value):
#     s=str(value)
#     if s.endswith("11"):
#         return 'th'
#     elif s.endswith("12"):
#         return 'th'
#     elif s.endswith("13"):
#         return 'th'
#     elif s.endswith("1"):
#         return 'st'
#     elif s.endswith("2"):
#         return 'nd'
#     elif s.endswith("3"):
#         return 'rd'
#     return 'th'    
    

# def ordinal(value):
#     return str(value) +ordinal_suffix(value)


    
def fetch_world():
    story=urlopen("http://sixty-north.com/c/t.txt")
    story_words=[]
    for line in story:
        line_words=line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    for word in story_words:
        print(word)
if __name__=='__main__':
    main()
                

    