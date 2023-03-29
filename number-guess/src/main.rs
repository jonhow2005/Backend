use std::io;

fn main() {
    println!("Hello! Welcome to our number guessing game!");
    println!("Please enter a number to guess.");
    
    let mut guess = String::new();
    
    io::stdin()
    	.read_line(&mut guess)
    	.expect("Failed to read line");
    	
    let guess: u32 = guess.trim().parse().expect("Please type a number!");
    	
    println!("You guessed: {}", guess);
    
    if guess == 42{
    	println!("You guessed the right number!");
    } else {
    	println!("You guessed the wrong number!");
    }    		
}
 	
