ransomNote = "aa"
magazine = "ab"

ransomCount = {"a": 2}
magazineCount = {"a": 1, "b": 1}
for i in ransomCount:
  if magazineCount["a"] >= ransomCount["a"]:
    print("True") 
  else:
    print("False") 