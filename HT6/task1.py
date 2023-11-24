words = {"найти", "lambdn"}
text = "тест в котором нужно найти подстроки с lambdn"

n = ({*filter(lambda x: x in text, words)})
print(n)
