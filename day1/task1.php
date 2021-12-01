#!/usr/bin/php
<?php

$file_str = file_get_contents( './input.txt' );
$inputs   = explode( "\n", $file_str );
$count    = 0;

for ( $i = 0; $i < count( $inputs ); $i++ ) {
    if ( $i > 0 && $inputs[ $i ] > $inputs[ $i-1 ] ) {
        $count++;
    }
}

echo $count;

?>