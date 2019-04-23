'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

def substring():
	s = "cbbd"
	reverse = s[::-1]
	print(s,reverse)

	for i in range(len(reverse)):
		for j in range(len(s)):
			if reverse[i] == s[j]:
				if i == 0:
					if reverse[i:-j] == s[j:]:

						return reverse[i:-j]
				else:
					if reverse[i:-j] == s[j:-i]:
						return reverse[i:-j]
	return None

if __name__ == "__main__":
	print(substring())



