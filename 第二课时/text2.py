jy=tuple('周杰伦',20,['football','music'])
print(jy.index(20))
element=20
if element in jy:
    index=jy.index(element)
    print(f"元素{element}存在于元组中，其索引为{index}")
else: