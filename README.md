![image info](./logo.png)

# About

The point of this exercise is to give you the chance to show us what you know, can do and how you approach problem solving.

For this exercise to be useful, we can't have solutions from the internet. This should go without saying, but please do not distribute or share this exercise to anyone in any form.


When you feel you're ready, please email us your solution and how we can run it. **In your email you must include that this is your original work and was completed only by you.**

# Instructions

This exercise comes in two parts. This is the first part, where you code on your own time. In the second part, we will ask you to come in and debug a similar code.

## Project setup

This assumes that you already have `Python 3` and `virtualenv` installed on your computer and you run the following commands in the project folder.

1. Create and activate a virtual environment by running
    
    ```
    virtualenv -p python3 <name of virtualenv>
    source <name of virtualenv>/bin/activate
    ```

2. Install the requirements

    ```
    pip install -r requirements.txt
    ```

3. Run the project

    ```
    python manage.py run
    ```

4. Project routes

    - GET: `/` : Main route
    - GET: `/api/v1/` : API home
    - POST: `/api/v1/boxfit/` : Endpoint to call in order to fit the text inside the box.

# Part I
## Make a text fit in a box

In this part we want you to determine the font size that will make some **text** fit inside a predefined box based on a particular font. We should be able to make the request to this endpoint: `/api/v1/boxfit/`. The code to this endpoint is located inside the file: `./app/controllers/text.py` 

The input data should look like this:

```json
{
    "facebook-header": {
        "copy": "dipp inc, thinking out of the box.",
        "x_start": 250,
        "y_start": 250,
        "max_width": 200,
        "max_height": 200,
        "font_url": "https://fonts.gstatic.com/s/cinzeldecorative/v7/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf"
    }
}
```

The API should respond with an output similar to the following:

```json
{
    "facebook-header": {
        "coordinates": {
            "height": 200,
            "width": 200,
            "x": 250,
            "y": 250
        },
        "splits": [
            {
                "content": "dipp inc,",
                "font_size": 27,
                "font_url": "https://fonts.gstatic.com/s/cinzeldecorative/v7/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf",
                "x": 250,
                "y": 250
            },
            {
                "content": "thinking",
                "font_size": 27,
                "font_url": "https://fonts.gstatic.com/s/cinzeldecorative/v7/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf",
                "x": 250,
                "y": 277
            },
            {
                "content": "out of the",
                "font_size": 27,
                "font_url": "https://fonts.gstatic.com/s/cinzeldecorative/v7/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf",
                "x": 250,
                "y": 304
            },
            {
                "content": "box.",
                "font_size": 27,
                "font_url": "https://fonts.gstatic.com/s/cinzeldecorative/v7/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf",
                "x": 250,
                "y": 331
            }
        ]
    }
}
```

As you may have noticed, you may need to break the copy into multiple lines or splits.

## Generate an image

In this part you will need to generate an image with the response obtained by calling your API.
It will look like this:

![Output](./output.png)

Take a look at the function `make_image` inside the file `./manage.py`. You can write your code to
call the API and make the image in the function. You can run the function by using the following command:

    python manage.py make_image


# Part II

In this part, we will ask you to come in and debug a similar code.

# Important notes:

- Fill free to use any library you want but don't forget to add it in `requirements.txt`
- There is no **right** or **wrong** answer. We are interested in how you approach problem solving.
- Please fill free to refactor the code if the structure does not fit your needs.
- Please don't hesitate email us if you have any questions.


# Good luck !!!
