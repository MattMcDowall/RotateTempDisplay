# RotateTempDisplay

The object of this project is to (semi-)automate all the common workflow steps for updating a temporary display within the library:
- Alma: Clear the Temporary Location from previous set of items
- Alma: Set Temporary Location on all items of new set
- Primo: Remove previous set of items from Primo Collection (if you have an associated Primo Collection)
- Primo: Add the new set's items to Primo Collection (ditto ⇑)

In practice, some of these steps can be performed simultaneously, but this is essentially the workflow that a person would follow.

## **Let me say up front . . .**
. . . that I'm relatively new and largely self-taught when it comes to both Git and Python. So I probably do things in not-the-most-efficient ways pretty regularly. If you have any advice for better methods to accomplish anything here, by all means please let me know.

## **Requirements**

- An Alma Set listing the items that are being **removed** from the location
- An Alma Set listing the items that are being **added** to the location
- If you wish to update an associated Primo Collection, of course, that collection needs to exist

> **Note:** It does not matter whether the Alma Sets are logical or itemized. The first set, in fact, can be a logical set which simply includes all items which have that specific temporary location.

### **Dependencies**
You'll need Python to run the script, of course. You will also need the `requests` and `xmltodict` packages.

## **A note on authentication**
You're also going to need appropriate API keys for your institution. Getting that set up is beyond the scope of this introduction, but I do want to mention how I've gone about implementing the authentication.

In order to keep the API credentials private, my approach is to tackle the authentication via an external file, and then call that file from these scripts.

What I've done is to create a script called `Credentials.py` which resides in this folder on my computer. To keep it private, I've added a line in the `.gitignore` file which filters it out of any pushes to the public repository. So you'll need to create your own Credentials.py file, in this same directory.

Credentials.py is a very simple file, looking like this:

    prod_api = 'a1aa11111111111111aa1a11aaaa11a111aa'
    sand_api = 'z9zzz99zzz99z9z999zzzzz999zz9999z999'

As you can see in the scripts themselves, we import that file thus:

    import Credentials

and get the API key for use thus:

    apikey = Credentials.prod_api

I hope that makes sense.
