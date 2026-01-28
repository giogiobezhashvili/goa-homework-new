
# .upper() - გადააქცევს მთელ ტექსტს დიდ ასოებად
# .lower() - გადააქცევს მთელ ტექსტს პატარა ასოებად
# .capitalize() - პირველ ასოს აქცევს დიდად, დანარჩენს პატარა ასოებად
# .capitalize() - პირველ ასოს აქცევს დიდად, დანარჩენს პატარა ასოებად

print("_______1_______")
word = input("შეიყვანე სიტყვა:")
print(word.lower())

print("_______2_______")
email = input("შეიყვანე შენი ემაილი:")
if "@" in email:
    print(email.upper())
else:
    print(f"ელფოსტა არა სწორია"+email.upper())
print("_______3_______")
book = input("შეიყვანე წიგნის სახელი:")
print(book.title())

print("_______4_______")
sentence = input("შეიყვანეთ წინადაედება")
symbol = input("შეიყვანეთ სიმბოლო: ")
print(sentence.count(symbol))

print("_______5_______")


word = input("შეიყვანეთ სიტყვა: ")
if word.isupper():
    print("სიტყვა უკვე დიდია!")
else:
    print(word.upper())







