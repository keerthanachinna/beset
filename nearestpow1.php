<?php

function nearestgreaterpowerof2($n)
{
    $res = 0;
    for ($i = $n; $i >= 1; $i--)
    {
        
        if (($i & ($i - 1)) == 0)
        {
            $res = $i;
            break;
        }
    }
    return $res;
}
$n=4;
echo nearestgreaterpowerof2
?>
