# AutoHotKey Writing Asisstant

This tool allows you to instantly generate AI text from a prompt by simply selecting it and using a keybind.

## Usage

### Flask

This project was build to be used with a flask server. Provided is a basic Flask server that interfaces with the Cloudflare worker API.

### AutoHotKey

Change the endpoint in the ahk script to the endpoint of your Flask server if you are hosting it externally.  
You may optionally compile the ahk script. Once ran, you can use `ctrl+;` to exit.  
To generate something, type then select your prompt text. Execute the program with `ctrl+'`, wait for a moment and watch your generated text be pasted.

***

Because AHK runs in the background, the icon can be completely hidden from viewing. Use this for convenience and not for any form of cheating.
