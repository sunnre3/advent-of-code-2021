#!/usr/bin/php
<?php

$file_str = file_get_contents( './input.txt' );
$inputs   = explode( "\n", $file_str );
$sums    = [];

for ( $i = 0; $i < count( $inputs ); $i++ ) {
    if ( isset( $inputs[ $i + 2 ] ) ) {
        $sums[] = (int) $inputs[ $i ] + (int) $inputs[ $i + 1 ] + (int) $inputs[ $i + 2 ];
    }
}

$count = 0;
for ( $i = 0; $i < count( $sums ); $i++ ) {
    if ( $i > 0 && $sums[ $i ] > $sums[ $i-1 ] ) {
        $count++;
    }
}

echo $count;

?>