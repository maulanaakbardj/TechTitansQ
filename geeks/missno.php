<?php
// PHP program to find
// the Missing Number

// getMissingNo takes array and
// size of array as arguments
function getMissingNo ($a, $n)
{
    $total = ($n + 1) * ($n + 2) / 2; 
    for ( $i = 0; $i < $n; $i++)
        $total -= $a[$i];
    return $total;
}

// Driver Code
$a = array(1, 2, 3, 5, 6);
$miss = getMissingNo($a, 5);
echo($miss);

?>
