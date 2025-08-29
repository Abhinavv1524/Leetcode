class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        vector<int> lastIndex(256, -1);
        int left = 0, maxlen = 0;

        for (int right = 0; right < s.size(); right++)
        {
            if (lastIndex[s[right]] >= left)
            {
                left = lastIndex[s[right]] + 1;
            }
            lastIndex[s[right]] = right;
            maxlen = max(maxlen, right - left + 1);
        }
        return maxlen;
    }
};