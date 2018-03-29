int lengthOfLongestSubstring(string s) {
        vector<int> flag(256,-1);
        int maxlen = 0,start = 0;
        for(int i = 0;i<s.length();++i)
        {
            if(flag[s[i]]<start)
            {
                maxlen = max(maxlen,i-start+1);
            }
            else
            {
                start = flag[s[i]]+1;
            }
	    flag[s[i]] = i;
        }
        return maxlen;
    }
