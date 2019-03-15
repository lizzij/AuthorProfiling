import wikipedia, re, string, sys

query = input("Please input query for wikipedia summary: ")

result = wikipedia.summary(query)
print(result)
