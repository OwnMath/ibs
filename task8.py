with open('file.txt', 'r') as f:
    with open('newfile.txt', 'w') as newf:
        text = f.read()
        reversedText = text[::-1]
        newf.write(reversedText)

        print(text, '\n', '-' * 50, '\n', reversedText)
