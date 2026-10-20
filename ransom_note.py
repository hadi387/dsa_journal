ransomNote = "aa"
magazine = "aab"
def canConstruct(ransomNote, magazine):
  ransomCount = {}
  for char in ransomNote:
      if char in ransomCount:
          ransomCount[char] = ransomCount[char] + 1
      else:
          ransomCount[char] = 1
  magazineCount = {}
  for char in magazine:
      if char in magazineCount:
          magazineCount[char] = magazineCount[char] + 1
      else:
          magazineCount[char] = 1

  for i in ransomCount:
    if magazineCount.get(i, 0) < ransomCount[i]:
      return False
  return True
print(canConstruct(ransomNote, magazine))