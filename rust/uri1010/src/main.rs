use std::io;

fn ler() -> (f32, f32) {
    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let mut iter = input.trim().split_whitespace();

    let _ = iter.next();
    let numero_pecas: f32 = iter.next().unwrap().parse().unwrap();
    let valor_unitario: f32 = iter.next().unwrap().parse().unwrap();
    (numero_pecas, valor_unitario)
}

fn calcular() -> f32 {
    let (n, v) = ler();
    n * v
}

fn main() {
    let mut valor_a_pagar: f32 = calcular();
    valor_a_pagar += calcular();
    println!("VALOR A PAGAR: R$ {:.2}", valor_a_pagar);
}
