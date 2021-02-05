# CscoopStockPrice
 
This program is designed for streaming Minecraft speedruns with price points to ruin the streamers run.
This is built from Youtube/Streamer Cscoop:
    Original Video: https://www.youtube.com/watch?v=T-OnamtkAYg&t=1397s

Prices are set to default $1, $2, $3, $4, $5, $6, $7

The prices can be changed upon running the program

To use in Streamlabs/OBS:
    1: Add a text object, for the content use "read from file"
    2: Select the first file for the lowest price, second file for the second lowest price, etc
        Reccomended: add "1 - *modifier* " then add a second text box with the 1.txt file contents
    3: open cmd and CD into the project file, run the stocklogic.py
    4: input the file number (hense the reccomended step for ease) to change the prices apon purchase
    