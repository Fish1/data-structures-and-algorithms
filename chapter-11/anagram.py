def generate_anagrams(word):
  if len(word) == 1:
    return [word[0]]

  result = []

  sub_anagrams = generate_anagrams(word[1:])

  for i in range(sub_anagrams):
    for j in range(len(sub_anagrams)):
      result.append(word[i] + sub_anagrams[j])  

  return result

print(generate_anagrams('abc'))