#! /usr/bin/env perl -0777 -nsw
my @array = m!\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b!ig;
my %hash = map { $_ => 1 } @array;
my @unique = sort(keys %hash);
$, = "\n";
print @unique;