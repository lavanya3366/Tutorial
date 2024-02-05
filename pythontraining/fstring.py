# name="lavanya"
# city="lucknow"
# # letter="hey my name is {1}. I am from {0}".format("lucknow","lavanya")
# # print(letter)
# print(f"hey my name is {name} and I am from {city}")

#not using fstring
# txt="for only {price:.2f} dollars!"
# print(txt.format(price=49.099999))

#using f-string
# price=49.099999
# txt=f"for only {price:.2f} dollars!"
# print(txt)

price=49.099999
txt=f"for only {{price:.2f}} dollars!"
print(txt)