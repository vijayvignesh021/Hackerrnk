void insertionSort2(int n, vector<int> arr) {
    int i = 1;
    int srt = 0;
    while(i < n)
    {
        if(arr[srt] > arr[i])
        {
        int comp = i;
        int revs =srt;
        int store = arr[i];
        while(store < arr[revs] and revs >= 0){
            arr[revs+1] = arr[revs];
            --comp;
            --revs;
        }
        arr[comp] = store;
        }
        for(int f = 0;f<n;++f)
        {
            cout<<arr[f]<<" ";
            }
        cout<<"\n";
        ++srt;
        ++i;
    }

}