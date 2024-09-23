import emoji

input_emoji = input("Input: ")
output = emoji.emojize(f"Output: {input_emoji}", language="alias")
print(output)