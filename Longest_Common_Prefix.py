'''
https://leetcode.com/problems/longest-common-prefix/
'''

def longestCommonPrefix(strs: list[str]) -> str:
    prefix=strs[0]
    finished=True
    while True:
        finished=True
        print(prefix)
        for word in strs[1:]:
            if not word.startswith(prefix):
                print('\tmissing',word)
                prefix=prefix[:-1]
                finished=False
                break
        if finished:
            print('finished')
            break
    return prefix

def longestCommonPrefix(strs):
    """
    Find the longest common prefix string amongst an array of strings.

    Args:
    strs (List[str]): A list of strings.

    Returns:
    str: The longest common prefix.
    """
    # Busco los prefijos partiendo de la palabramás corta
    pre = min(strs, key=len)
    
    # Recorro las palabras recortando el prefijo
    for i in strs:
        while not i.startswith(pre):
            pre = pre[:-1]
        if pre=="":
            break
    
    return pre 

print('Caso1:',longestCommonPrefix(["flower","flow","flight"]))

print('Caso2:',longestCommonPrefix(["dog","racecar","car"]))
