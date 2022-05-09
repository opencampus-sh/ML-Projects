use std::{path::PathBuf, io::{BufWriter, Write}, fs::File};

use image::{imageops, ImageBuffer, GrayImage, Luma};
use imageproc::drawing::draw_text_mut;
use rand::{thread_rng, Rng};
use rusttype::{Font, Scale};
use zzz::ProgressBarIterExt;

fn main() {
    //How many images to generate
    let images_to_generate = 10000;
    //Where to put them
    let imagedir = PathBuf::from("images");
    //Create folder if not already exists
    if !imagedir.exists(){
        std::fs::create_dir(&imagedir).unwrap();
    }
    //Create description file
    let mut description_file = BufWriter::new(File::create(imagedir.join("values.csv")).unwrap());
    //Write header
    writeln!(&mut description_file, "File,Value").unwrap();
    //Load font file
    let font = Font::try_from_bytes(include_bytes!("UbuntuMono-Regular.ttf")).unwrap();
    //Create handle to rng
    let mut rng = thread_rng();
    //Generate images
    for i in (0..images_to_generate).progress(){
        //Create new buffer, fill with white
        let mut img = GrayImage::new(640, 480);
        img.fill(255);

        //Create value
        let value = rng.gen_range(0.01 .. 129.99);
        //Round value
        let rounded = ((value * 100f64).round() / 100f64).to_string();

        //Text size and position
        let size = Scale::uniform(rng.gen_range(8.0 .. 48.0));
        let x = rng.gen_range(32 .. 500);
        let y = rng.gen_range(32 .. 350);

        draw_text_mut(&mut img, Luma([0]), x, y, size, &font, &rounded);
    
        let filename = format!("{i}.jpg");
    
        img.save(imagedir.join(&filename)).unwrap();

        writeln!(&mut description_file, "{filename},\"{rounded}\"").unwrap();
    }

    println!("Done.");

    //Second copy of this program to create single digits

    //How many images to generate
    let images_to_generate = 10000;
    //Where to put them
    let imagedir = PathBuf::from("digits");
    //Create folder if not already exists
    if !imagedir.exists(){
        std::fs::create_dir(&imagedir).unwrap();
    }
    //Create description file
    let mut description_file = BufWriter::new(File::create(imagedir.join("values.csv")).unwrap());
    //Write header
    writeln!(&mut description_file, "File,Value").unwrap();
    //Load font file
    let font = Font::try_from_bytes(include_bytes!("UbuntuMono-Regular.ttf")).unwrap();
    //Create handle to rng
    let mut rng = thread_rng();
    //Generate images
    for i in (0..images_to_generate).progress(){
        //Create new buffer, fill with white
        let mut img = GrayImage::new(640, 480);
        img.fill(255);

        //Create value
        let value: i32 = rng.gen_range(0 .. 10);
        //Round value
        let rounded = value.to_string();

        //Text size and position
        let size = Scale::uniform(rng.gen_range(8.0 .. 48.0));
        let x = rng.gen_range(32 .. 500);
        let y = rng.gen_range(32 .. 350);

        draw_text_mut(&mut img, Luma([0]), x, y, size, &font, &rounded);
    
        let filename = format!("{i}.jpg");
    
        img.save(imagedir.join(&filename)).unwrap();

        writeln!(&mut description_file, "{filename},\"{rounded}\"").unwrap();
    }

    println!("Done.");

    

}
