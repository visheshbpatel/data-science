import requests
import webbrowser
import io
from tkinter import *
from PIL import ImageTk, Image


class NewsApp:
    def __init__(self):
        url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=YOUR_API_KEY"
        self.articles = requests.get(url).json()["articles"]
        self.index = 0

        self.root = Tk()
        self.root.geometry("400x650")
        self.root.title("News App")

        self.show_news()
        self.root.mainloop()

    def show_news(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        article = self.articles[self.index]

        # Image
        try:
            img_data = requests.get(article["urlToImage"]).content
            image = Image.open(io.BytesIO(img_data))
            image.thumbnail((400, 250))
            photo = ImageTk.PhotoImage(image)

            label = Label(self.root, image=photo)
            label.image = photo
            label.pack()
        except:
            pass

        # Title
        Label(
            self.root,
            text=article["title"],
            wraplength=380,
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # Description
        Label(
            self.root,
            text=article["description"],
            wraplength=380
        ).pack(pady=10)

        # Buttons
        frame = Frame(self.root)
        frame.pack(pady=20)

        if self.index > 0:
            Button(frame, text="Previous",
                   command=lambda: self.change_news(-1)).pack(side=LEFT)

        Button(frame, text="Read More",
               command=lambda: webbrowser.open(article["url"])).pack(side=LEFT, padx=10)

        if self.index < len(self.articles) - 1:
            Button(frame, text="Next",
                   command=lambda: self.change_news(1)).pack(side=LEFT)

    def change_news(self, step):
        self.index += step
        self.show_news()


NewsApp()