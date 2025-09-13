# WAP to create file and insert data
with open("practice.txt" , "w") as f:
    f.write("hii\n")
    f.write("I am learning python")
    f.write("\nfrom apna college")
    f.write("\nusing Java.\nI like programming in Java")


# WAF to replace java from python
with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(data)
print(new_data)

# WAF to find word "learning" in practice.txt
def check_for_word():
    word = 'learning'
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
            print("not found")

check_for_word()