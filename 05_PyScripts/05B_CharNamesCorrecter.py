def string_appender(name, append_str):
    return "%s_%s" % (name, append_str)

if __name__ == '__main__':
    name_list = ["kenny", "hippo", "peter", "kelly", "john", "bob"]
    funcs = []
    for name in name_list:
        funcs.append(lambda n=name: string_appender(n, "char"))
    # Don’t modify the code below:
    for f in funcs:
        print(f())