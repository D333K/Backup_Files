import operations

print("Welcome To Backup Files Program:-")
print('-' * 50)

src = input("Source Folder: ")
dst = input("Destination Folder: ")

operations.backup_files(src, dst)
