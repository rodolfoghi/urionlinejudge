use std::io;

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .unwrap();
    let raio: f64 = input
                        .trim()
                        .parse()
                        .unwrap();
    let area: f64 = 3.14159 * (raio * raio);
    println!("A={:.4}", area);
}
