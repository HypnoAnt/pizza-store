# Project 1  Forms & Redirection (2024/2025)

There are some aspects of this you will not be able to complete until the lectures in Week 4

A key part of building your final year projects are creating apps that require user input and redirection.  This assignment should be **completed individually**.

You are going to be creating a pizza ordering system in Django. The steps are

1. A user creates an account on your webapp
2. The are then presented with a page showing all their previous orders and a link to create a new order
3. They are then redirected to a page where they are asked to create a pizza
4. They are then redirected to another page asking them to fill out
    - Their name
    - address
    - payment info
5. After entering all information they are then presented with a final page showing the details of their order including
    1. The address and date/time of the delivery
    2. Details on the pizza they ordered, size, toppings etc…

## Create pizza page

On the create pizza page a user should be able to

- Select the size of the pizza they want (small, medium, large etc..)
- Select the pizza crust type (normal, thin, thick, gluten free etc..)
- Select the pizza sauce (tomato, bbq etc..)
- Select the cheese (Mozzarella, Vegan , Low fat etc..)
- Select from the following toppings (you can add more , but these have to be there at minimum):
    - Pepperoni
    - Chicken
    - Ham
    - Pineapple
    - Peppers
    - Mushrooms
    - Onions

## Delivery details page

Once they are finished building their pizza they should be able to click a button called “Order” , here they are taken to the order page where they will be asked for

- Their name
- Their address
- Their card number
- Their card expiry date (Month, Year)
- Their card cvv

🚨 The information on this page should be **validated** i.e. no blank expiration date, no blank Number etc.. https://data-flair.training/blogs/django-forms-handling-and-validation/


If the form is completed without errors they will be redirected to another page confirming that their order is complete and show them the pizza they just created.

Finally, an admin using the django `admin`interface should be able to:

- Create new pizza sizes
- Add new types of cheese
- Add new types of sauces

# Steps

Get into your groups and start to plan your app, think about

- What models do we have (what needs to get stored in the database)?
- What are the pages of the app
    - Each page needs a `template`
    - Each page needs its own `path` in [`urls.py`](http://urls.py)
        - Each `path`needs its own view in [`views.py`](http://views.py)
- What forms are needed in [`forms.py`](http://forms.py) - what are their rules?
- What is the design of our app , header/footer - remember to install bootstrap and check what [components](https://getbootstrap.com/2.3.2/components.html) you can use to help make the app

# Styling

You should use bootstrap (or any other css framework of your choice) and style your page marks will be awarded for student who demonstrate use of components and invest time into the styling of their webpage

[Accordion](https://getbootstrap.com/docs/5.3/components/accordion/)

# Hints & Tips

Model & form design are the key to this app

- A list of all model data types can be found here: https://docs.djangoproject.com/en/4.1/ref/models/fields/
- All forms should be [ModelForms](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)
- For toppings, initially you should think of them as checkboxes , this would mean they are “BooleanFields” in `models.py`

# Submission

For your assignment you are to submit the following:

One zip file on loop containing the following

- A link to a recorded video of you demonstrating your app (inside a .txt file)
- Your project code

**This project is worth 10% of your overall grade**

# Video demonstration

For the video demonstration it is required that you use your microphone. In the video you should show the code and explain the following:

- Your [Models.py](http://Models.py) file- what are the models you created and how do they link together
- Your [urls.py](http://urls.py) file, explain the links you have created and where the are used
- The files [forms.py](http://forms.py) and [views.py](http://views.py) , explain how the forms are linked to your views, and where in the views.py you use different forms
- The structure of your [templates](http://templates.py) files (html)

In addition you should walk through the functionality of the application running, showing the following:

- Creating a new order
- Checking out
- The order complete page

The video should be no more than 5 miuintes, this is a hard limit, a penalty of 5% applies to all who go over the limit.

# Marking scheme:

Below is the marking scheme, attempt marks will be provided for semi-working functionality.

| Name         | Description                                                                                                                                                                                                                                                                                                                | Marks |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Model Design | - How well are modules structured? - Are relationships (Foreign Keys) correct? (https://blog.devgenius.io/design-relationships-between-django-models-11ce7960e2ec) - Are the right datatypes assigned to each property?  (https://www.webforefront.com/django/modeldatatypesandvalidation.html) - Are default values used? | 15%   |
| Views.py     | - Do views run properly (i.e. they do not crash)| 10%   |
| Templates    | - Is the HTML/CSS/JS Correct ? |       | - Is there a proper template structure (e.g. `base.html` )  | 10% |
| Forms | - Are all necessary fields shown - Does validation work as intended - are all fields validated properly ?  | 15% |
| Create order | - Can a user create an order for a pizza without error - Can multiple users create an order for a pizza without error - Can a single user order multiple pizzas without error | 10% |
| Checkout | - Can a user enter their payment info - Is a users payment info validated (e.g. no empty fields)  | 15% |
| Order complete | - Is a user redirected to an order complete page, showing the details of an order automatically | 5% |
| Video | Video containing demonstration of app and walkthrough of code | 15% |

# Deadline

The deadline for submission is Friday the **$14^{th}$ of February at 11:59PM**. Extensions will only be granted under mitigating circumstances.

If you are making a late submission, email me your submission directly, the submission form of loop will close after the deadline.

# Penalties

- The penalty for late submission is 10% **per day** past the deadline.
- If your video cannot be viewed, you will lose **15%**. To make sure that the video is accessible, copy/paste the link into an incognito window and make sure it can be viewed.
    - The link to the video **must**  be in the .zip file. If it is not in the .zip file you will not be awarded marks. Any alternative method of submitting the video link will be **ignored.**
- If you include artefacts that should not be inside your zip file, including node_modules, python environments, .git directories you will lose an additional 5%.
