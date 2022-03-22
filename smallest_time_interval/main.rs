/*
Given a list of times in a 24-hour period, return the smallest interval between two times in the list. Hint: you can do 
this in O(n) time!

Example:

$ smallestTimeInterval(["01:00", "08:15", "11:30", "13:45", "14:10", "20:05"])
$ "25 minutes"
*/
//----------------------------------------------------------------------------------------------------------------------

use std::mem;
use std::cmp;
use indexmap::indexmap;
//----------------------------------------------------------------------------------------------------------------------

macro_rules! get_bit {
    ($array:expr, $pos:expr) => {{
        let size_len = mem::size_of_val(&$array[0]) * 8;
        ($array[$pos / size_len] & (1 << (size_len - 1 - $pos % size_len))) > 0
    }};
}
//----------------------------------------------------------------------------------------------------------------------

macro_rules! set_bit {
    ($array:expr, $pos:expr) => {{
        let size_len = mem::size_of_val(&$array[0]) * 8;
        $array[$pos / size_len] |= 1 << (size_len - 1 - $pos % size_len); 
    }};
}
//----------------------------------------------------------------------------------------------------------------------

fn get_smallest_time_interval(vector: &mut Vec<&str>) -> usize {
    const MAX_BITS: usize = 24 * 60;
    const MAX_BYTES: usize = MAX_BITS / 32;
    let mut minutes_helper: [u32; MAX_BYTES] = [0; MAX_BYTES];
    for time in vector.iter() {
        let mut time_splitted: Vec<&str> = time.split(':').collect();
        let minute = time_splitted.pop().unwrap().parse::<usize>().unwrap();
        let hour = time_splitted.pop().unwrap().parse::<usize>().unwrap();
        let idx = (hour * 60) + minute;
        match get_bit!(minutes_helper, idx) {
            true  => { return 0; }
            false => { set_bit!(minutes_helper, idx); }
        }
    }
    let (mut smallest, mut last_index) = (MAX_BITS, MAX_BITS);
    for i in 0..MAX_BITS {
        if get_bit!(minutes_helper, i) {
            if last_index != MAX_BITS {
                smallest = cmp::min(smallest, i - last_index);
                if smallest == 1 { break; }
            }
            last_index = i;
        }
    }
    return smallest;
}
//----------------------------------------------------------------------------------------------------------------------

fn main() {
    let mut examples = indexmap! {
        "ex1" => vec!["01:00", "08:15", "11:30", "13:45", "14:10", "20:05"]
    };
    for (key, ex) in examples.iter_mut() {    
        let smallest = get_smallest_time_interval(ex);
        println!("[{}]: {:?} == {} minutes", key, ex, smallest);
    }
    println!();
}
//----------------------------------------------------------------------------------------------------------------------

