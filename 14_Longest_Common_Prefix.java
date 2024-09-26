// https://leetcode.com/problems/longest-common-prefix

class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        for (int i = 0; i < strs[0].length(); i++) {
            for (String s : strs) {
                if (s.length() - 1 < i) {
                    return prefix;
                }
                if (!(strs[0].charAt(i) == s.charAt(i))) {
                    return prefix;
                }
            }
            prefix += strs[0].charAt(i);
        }
        return prefix;
    }
}
