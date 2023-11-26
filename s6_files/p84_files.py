my_file = open('data.txt', 'r')
my_file_content = my_file.read()

my_file.close()
print(my_file_content)

user_name = input('Név: ')
my_file_w = open('data.txt', 'w')

my_file_w.write(user_name)
my_file_w.close()
