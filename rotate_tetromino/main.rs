/*
Given a matrix of 0s and 1s where 1s represent a Tetris block, and a rotation direction, return the matrix with the 
block rotated once. You can use this guide for a hint to the algorithm!

Example:

let grid = [
[0,1,0,0],
[0,1,1,1],
[0,0,0,0],
[0,0,0,0]
]

$ rotateTetromino(grid, 'clockwise')
$ [
[0,0,1,1],
[0,0,1,0],
[0,0,1,0],
[0,0,0,0]
]
*/
//----------------------------------------------------------------------------------------------------------------------

use std::cmp;
use indexmap::indexmap;
//----------------------------------------------------------------------------------------------------------------------

enum Rotation {
    CLOCKWISE,
    ANTICLOCKWISE,
}
//----------------------------------------------------------------------------------------------------------------------

impl Rotation {
    fn as_str(&self) -> &'static str {
        match self {
            Rotation::CLOCKWISE => "clockwise",
            Rotation::ANTICLOCKWISE => "anticlockwise"
        }
    }
}
//----------------------------------------------------------------------------------------------------------------------

fn transpose_mat<const N: usize, const M: usize>(
    matrix: &mut [[i32; M]; N], min_i: usize, min_j: usize, len: usize
) {
    for i in 0..len {
        for j in i..len {
            (matrix[min_i + j][min_j + i], matrix[min_i + i][min_j + j]) = 
            (matrix[min_i + i][min_j + j], matrix[min_i + j][min_j + i]);
        }
    }
}
//----------------------------------------------------------------------------------------------------------------------

fn reverse_horizontal_mat<const N: usize, const M: usize>(
    matrix: &mut [[i32; M]; N], min_i: usize, min_j: usize, len: usize
) {
    for i in 0..len {
        for j in 0..len/2 {
            (matrix[min_i + i][min_j + j], matrix[min_i + i][min_j + len - 1 - j]) = 
            (matrix[min_i + i][min_j + len - 1 - j], matrix[min_i + i][min_j + j]);
        }
    }
}
//----------------------------------------------------------------------------------------------------------------------

fn rotate_square_mat_90<const N: usize, const M: usize>(
    matrix: &mut [[i32; M]; N], min_i: usize, min_j: usize, len: usize, rotation: Rotation
) {
    match rotation {
        Rotation::CLOCKWISE => {
            transpose_mat(matrix, min_i, min_j, len);
            reverse_horizontal_mat(matrix, min_i, min_j, len);
        }
        Rotation::ANTICLOCKWISE => {
            reverse_horizontal_mat(matrix, min_i, min_j, len);
            transpose_mat(matrix, min_i, min_j, len);
        }
    }
}
//----------------------------------------------------------------------------------------------------------------------

fn rotate_block_90<const N: usize, const M: usize>(matrix: &mut [[i32; M]; N], rotation: Rotation) {
    let (mut min_i, mut min_j, mut len): (usize, usize, usize) = (N, M, 0);
    let (mut sum_i, mut sum_j, mut count) = (0, 0, 0);
    for i in 0..N {
        for j in 0..M {
            if matrix[i][j] != 0 {
                let diffi = if i >= min_i { i - min_i + 1 } else { 0 };
                let diffj = if j >= min_j { j - min_j + 1 } else { 0 };
                len = cmp::max(len, cmp::max(diffi, diffj));
                min_i = cmp::min(min_i, i);
                min_j = cmp::min(min_j, j);
                sum_i += i;
                sum_j += j;
                count += 1;
            }
        }
    }
    let center_i = (sum_i as f32 / count as f32).round() as usize;
    let center_j = (sum_j as f32 / count as f32).round() as usize;
    min_i = if center_i >= (len / 2) { center_i - (len / 2) } else { 0 };
    min_j = if center_j >= (len / 2) { center_j - (len / 2) } else { 0 };
    min_i = if min_i + len > N { N - len } else { min_i };
    min_j = if min_j + len > M { M - len } else { min_j };
    rotate_square_mat_90(matrix, min_i, min_j, len, rotation);
}
//----------------------------------------------------------------------------------------------------------------------

fn pretty_print_mat<const N: usize, const M: usize>(matrix: &[[i32; M]; N]) {
    for i in 0..N {
        print!("[ ");
        for j in 0..M-1 {
            print!("{}, ", matrix[i][j]);
        }
        if M > 0 {
            print!("{} ", matrix[i][M-1]);
        }
        println!("]");
    }
    println!();
}
//----------------------------------------------------------------------------------------------------------------------

fn main() {
    let mut examples = indexmap! {
        "ex1" => [
            [0, 1, 0, 0], 
            [0, 1, 1, 1], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0],
        ],
        "ex2" => [
            [0, 0, 1, 1], 
            [0, 0, 1, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 0],
        ],
        "ex3" => [
            [0, 0, 0, 0], 
            [0, 1, 1, 1], 
            [0, 0, 0, 1], 
            [0, 0, 0, 0],
        ],
        "ex4" => [
            [0, 0, 1, 0], 
            [0, 0, 1, 0], 
            [0, 1, 1, 0], 
            [0, 0, 0, 0],
        ],
        "ex5" => [
            [0, 0, 1, 0], 
            [0, 0, 1, 0], 
            [0, 0, 1, 0], 
            [0, 0, 1, 0],
        ],
        "ex6" => [
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [1, 1, 1, 1], 
            [0, 0, 0, 0],
        ],
        "ex7" => [
            [0, 1, 0, 0], 
            [0, 1, 0, 0], 
            [0, 1, 0, 0], 
            [0, 1, 0, 0],
        ],
        "ex8" => [
            [0, 0, 0, 0], 
            [1, 1, 1, 1], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0],
        ],
        "ex9" => [
            [0, 0, 0, 0], 
            [0, 1, 1, 0], 
            [0, 0, 1, 1], 
            [0, 0, 0, 0],
        ],
        "ex10" => [
            [0, 0, 0, 0], 
            [0, 0, 1, 0], 
            [0, 1, 1, 0], 
            [0, 1, 0, 0],
        ],
        "ex11" => [
            [0, 0, 0, 0], 
            [0, 1, 1, 0], 
            [0, 0, 1, 1], 
            [0, 0, 0, 0],
        ],
        "ex12" => [
            [0, 0, 0, 0], 
            [0, 0, 0, 1], 
            [0, 0, 1, 1], 
            [0, 0, 1, 0],
        ],
        "ex13" => [
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 1, 1, 0], 
            [0, 0, 1, 1],
        ],
        "ex14" => [
            [0, 1, 1, 0], 
            [0, 1, 1, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0],
        ],
        "ex15" => [
            [0, 0, 1, 1], 
            [0, 0, 1, 1], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0],
        ],
        "ex16" => [
            [0, 0, 1, 0], 
            [0, 1, 1, 1], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0],
        ],
        "ex17" => [
            [0, 0, 1, 0], 
            [0, 1, 1, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 0],
        ],
        "ex17" => [
            [0, 0, 0, 0], 
            [0, 1, 1, 1], 
            [0, 0, 1, 0], 
            [0, 0, 0, 0],
        ],
        "ex18" => [
            [0, 0, 1, 0], 
            [0, 0, 1, 1], 
            [0, 0, 1, 0], 
            [0, 0, 0, 0],
        ],
        "ex19" => [
            [0, 0, 1, 0], 
            [0, 0, 1, 1], 
            [0, 0, 1, 0], 
            [0, 0, 0, 0],
        ]
    };
    for (key, mut ex) in examples.iter_mut() {     
        // pretty_print_mat(&mut ex);
        println!("{}:", key);
        rotate_block_90(&mut ex, Rotation::CLOCKWISE);
        pretty_print_mat(&mut ex);
    }
    println!();
}
//----------------------------------------------------------------------------------------------------------------------

