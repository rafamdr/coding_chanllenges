/*
Given an integer n representing the number of sides of a regular polygon, return the measure of each interior angle. 
Bonus points: implement some of the other functions listed in the linked Wikipedia page!

Example:

$ interiorAngleSize(3)
$ 60 // Each angle in a triangle that is a regular polygon is 60 degrees

$ interiorAngleSize(8)
$ 135
*/
//----------------------------------------------------------------------------------------------------------------------


use std::f64::consts::PI;
//----------------------------------------------------------------------------------------------------------------------

#[derive(Default)]
struct RegularPolygon {
    n: usize,
    side: f64,
    diagonals: usize,
    perimeter: f64,
    internal_angle: f64,
    internal_angle_sum: f64,
    polygon_area: f64,
    circumradius: f64,
    circumcircle_area: f64,
    inscribed_radius: f64,
    inscribed_area: f64,
}

trait AdditionalProperties {
    fn recalculate_properties(&mut self, n: usize, side: f64);
}

impl AdditionalProperties for &mut RegularPolygon {
    fn recalculate_properties(&mut self, n: usize, side: f64) {
        (self.n, self.side) = (n, side);
        if self.n > 2 {
            self.diagonals = (self.n * (self.n - 3)) / 2;
            self.perimeter = (self.n as f64) * side;
            self.internal_angle = (self.n as f64 - 2.0) * (PI / self.n as f64);
            self.internal_angle_sum = self.internal_angle * self.n as f64;
            self.polygon_area = (1.0 / 4.0) * (self.n  as f64) * self.side.powi(2) * (PI / self.n as f64).tan().recip();
            self.circumradius = self.side / (2.0 * (PI / self.n as f64).sin());
            self.circumcircle_area = PI * self.circumradius.powi(2);
            self.inscribed_radius = self.side / (2.0 * (PI / self.n as f64).tan());
            self.inscribed_area = PI * self.inscribed_radius.powi(2);
        }
    }
}

impl RegularPolygon {
    fn new(n: usize, side: f64) -> RegularPolygon {
        let mut polygon: RegularPolygon = Default::default();
        (&mut polygon).recalculate_properties(n, side);
        return polygon;
    }
}
//----------------------------------------------------------------------------------------------------------------------

fn main() {
    let polygon = RegularPolygon::new(7, 2.0);
    println!("Num. of sides: {}", polygon.n);
    println!("Side size: {}", polygon.side);
    println!("Num. of diagonals: {}", polygon.diagonals);
    println!("Perimeter: {}", polygon.perimeter);
    println!("Internal Angle Deg: {}", polygon.internal_angle.to_degrees());
    println!("Internal Angle Sum Deg: {}", polygon.internal_angle_sum.to_degrees());
    println!("Circumradius: {}", polygon.circumradius);
    println!("Inscribed Radius: {}", polygon.inscribed_radius);
    println!("Polygon Area: {}", polygon.polygon_area);
    println!("Circumcircle Area: {}", polygon.circumcircle_area);
    println!("Inscribed Area: {}", polygon.inscribed_area);
    println!();
}
//----------------------------------------------------------------------------------------------------------------------

