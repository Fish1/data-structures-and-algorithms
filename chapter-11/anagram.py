def anagrams_of(string):
  if len(string) == 1:
    return string[0]
  
  collection = []

  substring_anagrams = anagrams_of(string[1:])

  for substring in substring_anagrams:
    for index in range(len(substring) + 1):
      collection.append(substring[:index] + string[0] + substring[index:])