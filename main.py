"""Creates and runs the application. This is the starting module of the program."""

from application import Application

try:
    #create a test application object
    app = Application()

    #run the application
    app.run()
except Exception as ex:
    print(f"An unexpected error ocurred in the program. Please contact your administrator.\nError Message: {ex}")
