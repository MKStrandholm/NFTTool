# Python Pixel NFT Tool
A modified version of the open-source BitBirds python code that I used to generate a sample NFT collection.

# ! NOTE !
In order for this script to work, a folder named 'minimos' is required as that folder is hardcoded for the output. Create a new folder called 'minimos' in the root folder and it should generate the images as intended.

# What does it do?
In essence, this tool utilizes the core components of the BitBirds code in order to generate a pixel art image using a matrix of RGB values. However, I wanted to further customize it by creating 'layers' that can be generated independently of one another based on different odds.

# How does it work?
By creating separate JS files, I was able to code out the desired layer styles and then, through importing into the main file I had the freedom to mix and match through random generation. 

As for the layers themselves, I used a technique in order to effectively transpose the layers ontop of one other. Simply put, to replicate an alpha channel on each layer, I used rgb(0,0,0) as a 'transparent' pixel which would be ignored when merging layers. This meant that only visible colors and intended pieces were overlaid onto the previous layer, creating a fully composed image.

# Example
![image](https://user-images.githubusercontent.com/15320504/144395855-e2bb14ed-3592-4cc1-a4c7-504c050716ba.png)

