# open and read input file
set file_data [read [open "day1_input.txt" r]]

#  Process data file
set data [split $file_data "\n"]

set temp_sum 0
# compute each elf's calories
foreach line $data {
    if { $line != "" } {
        set temp_sum [expr $temp_sum + $line]
    } elseif { $line == "" } {
        scan $temp_sum %d temp_sum
        lappend list $temp_sum
        set temp_sum 0
    }
    
}
# sort and find
set newlist [lsort -integer -decreasing $list]
puts $newlist
#find highest value in list
set max1 [lindex $newlist 0]
# answer 1
puts $max1
#find 2nd highest value in list
set max2 [lindex $newlist 0]
#find 3rd value in list
set max3 [lindex $newlist 0]
# answer 2
puts [expr $max1 + $max2 + $max3]