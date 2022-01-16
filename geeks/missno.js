<script>
 
    // Function to get the missing number
    function getMissingNo(a, n) {
 
        let total = Math.floor((n + 1) * (n + 2) / 2);
        for (let i = 0; i < n; i++)
            total -= a[i];
        return total;
    }
 
    // Driver Code

    let arr = [ 1, 2, 3, 5, 6 ];
    let n = arr.length;
    let miss = getMissingNo(arr, n);
    document.write(miss);

// This code is contributed by Surbhi Tyagi 

</script>
