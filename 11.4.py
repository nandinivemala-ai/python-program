d={'apple':5,'banana':10,'orange':8,'mango':15}
kid=['apple','banana']
for k in kid:
    if k in d:
        del d[k]
        print(d)
