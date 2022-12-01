# proc to find max value in list
proc findmax { items } {
    set max 0
    foreach cal $items {
        if { $cal > $max } {
            set max $cal
        }
    }
    return $max
}

# open and read input file
set fp [open "day1_input.txt" r]
set file_data [read $fp]
close $fp

#  Process data file
set data [split $file_data "\n"]

# set holding variables
set temp_sum 0
set num 1
set list {}
set save1 1
set max1 0
set save2 1
set max2 0
set save3 1
set max3 0

# compute each elf's calories
foreach line $data {
    if { $line != "" } {
        set temp_sum [expr $temp_sum + $line]
    } elseif { $line == "" } {
        lappend list $temp_sum
        set num [expr $num + 1]
        set temp_sum 0
    }
    
}

#find highest value in list
set max1 [findmax $list]
# answer 1
puts $max1
#remove from list to find next highest
set idx [lsearch $list $max1]
set list [lreplace $list $idx $idx]
#find highest value in list
set max2 [findmax $list]
#remove from list to find next highest
set idx [lsearch $list $max2]
set list [lreplace $list $idx $idx]
#find highest value in list
set max3 [findmax $list]
# answer 2
puts [expr $max1 + $max2 + $max3]

