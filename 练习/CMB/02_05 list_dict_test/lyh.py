def num_to_english(num):
    english_num_list=["zero","one","two","three","four","five","six","seven","eight","nine"]
    new_str=str(num)[::-1]
    new_num_str=[]
    for str_num in new_str:
        new_num_str.append(english_num_list[int(str_num)])
    return "-".join(new_num_str)
num=637
print(num_to_english(num))

def list_map(list1,list2):
    target_dict={}
    for num in list1:
        for string in list2[::-1]:
            if len(string)==num:
                target_dict[num]=string
                break
    return target_dict

list1=[4,7,2,5,9]
list2=["f","43","f2","fgde32e","4322","34aasdasa"]
print(list_map(list1,list2))

def sort_dict(orgin_list):
    new_list=sorted(orgin_list,key=lambda x:x["name"],reverse=False)
    for i in range(len(new_list)-1):
        for j in range(len(new_list)-1-i):
            if new_list[j]["name"]==new_list[j+1]["name"] and new_list[j]["num"]<new_list[j+1]["num"]:
                tem=new_list[j]
                new_list[j]=new_list[j+1]
                new_list[j+1]=tem
    return new_list
orgin_dict=[{"name":"Jack","num":"1324"},{"num":"AA11","name":"Liu"},{"num":"AA12","name":"Johnson"},{"num":"AA21","name":"Johnson"},{"num":"HH23","name":"Johnson"},{"num":"1151","name":"Li"}]
print(sort_dict(orgin_dict))
