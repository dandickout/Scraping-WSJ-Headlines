from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import tkinter as tk

website = "https://www.wsj.com/news/technology"
path = "C:\CarbonBlock\Applications\chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("headless")


# Function to scrape the headlines from the BBC News website
def scrape_headlines():
    # Make a request to the website
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, chrome_options=options)
    driver.get(website)

    # Parse the HTML content of the page
    containers = driver.find_elements(by="xpath", value='//*[@id="top-news"]/div/div//h3')

    # Extract the text of each headline
    headlines = []
    for container in containers:
        title = container.find_element(by="xpath", value='./a').text
        link = container.find_element(by="xpath", value='./a').get_attribute("href")
        print(title)
        print(link)
        headlines.append(title)

    #return the list of headlines
    return headlines

# Function to update the headlines in the pop-up window
def update_headlines():
    # Scrape the headlines from the website
    headlines = scrape_headlines()

    # Clear the current headlines from the window
    for widget in window.winfo_children():
        widget.destroy()

    # Add the new headlines to the window
    for headline in headlines:
        label = tk.Label(window, text=headline, font=("Helvetica", 14))
        label.pack()

    # Schedule the next update in 60 seconds
    window.after(60000, update_headlines)

# Create the pop-up window
window = tk.Tk()
window.title("WSJ News Headlines")

# Update the headlines for the first time
update_headlines()

# Run the tkinter event loop
window.mainloop()
