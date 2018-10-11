abc = "abc"
abc_list = list(abc)
print(abc_list)

idx = "apple".find("l")  ## return 3, if not found, return -1
print(idx)

split_lst = "Hello world!".split() ## if sep == None: words are separated by arbitrary strings of whitespace characters
print(split_lst)
join_lst = "_".join(abc_list)
print(join_lst)

