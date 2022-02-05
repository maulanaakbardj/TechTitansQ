/*Longest substring without repeat 
  vector<bool> visited(26);
    for (int k = i; k <= j; k++) {
        if (visited[str[k] - 'a'] == true)
            return false;
        visited[str[k] - 'a'] = true;
    }
  return true;*/
    int left=0;
    map<char,int>m;
    int right=0;
    int n=s.length();
    int len=0;
    while(right<n)
    {
        if(m.find(s[right])!=m.end())
        {
            left=max(m[s[right]]+1,left);
        }

        m[s[right]]=right;
        len=max(len,right-left+1);
        right++;


    }

    return len;


}
