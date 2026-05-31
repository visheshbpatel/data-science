import requests
import webbrowser
import io
import os
import threading
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


class NewsApp:
    def __init__(self):

        self.colors = {
            "bg": "#0B0B0C",
            "text": "#F5F5F7",
            "muted": "#A1A1AA",
            "blue": "#2563EB",
            "green": "#10B981"
        }

        self.root = Tk()
        self.root.geometry("332x646")
        self.root.configure(bg=self.colors["bg"])
        self.root.title("NewsFlash")
        self.root.resizable(False, False)

        self.articles = []
        self.index = 0
        self.image_cache = {}

        self.show_loading()

        # load in background
        threading.Thread(
            target=self.fetch_news,
            daemon=True
        ).start()

        self.root.mainloop()

    def show_loading(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        Label(
            self.root,
            text="📰",
            font=("Helvetica", 40),
            bg=self.colors["bg"],
            fg="white"
        ).pack(pady=(180, 12))

        Label(
            self.root,
            text="Loading News...",
            font=("Helvetica", 15, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack()

        Label(
            self.root,
            text="Fetching latest headlines",
            font=("Helvetica", 10),
            bg=self.colors["bg"],
            fg=self.colors["muted"]
        ).pack(pady=8)

    def fetch_news(self):

        try:
            url = (
                f"https://newsapi.org/v2/everything?"
                f"q=india&sortBy=publishedAt&language=en"
                f"&pageSize=20&apiKey={api_key}"
            )

            response = requests.get(
                url,
                timeout=8
            )

            self.articles = response.json().get(
                "articles",
                []
            )

            self.root.after(
                0,
                self.show_news
            )

        except:
            self.root.after(
                0,
                self.show_error
            )

    def fetch_image(self, url):

        if not url:
            return None

        if url in self.image_cache:
            return self.image_cache[url]

        try:
            img_data = requests.get(
                url,
                timeout=5
            ).content

            image = Image.open(
                io.BytesIO(img_data)
            )

            image = image.resize(
                (300, 190),
                Image.LANCZOS
            )

            photo = ImageTk.PhotoImage(image)

            self.image_cache[url] = photo

            return photo

        except:
            return None

    def format_date(self, date_string):

        try:
            dt = datetime.strptime(
                date_string,
                "%Y-%m-%dT%H:%M:%SZ"
            )
            return dt.strftime(
                "%d %b %Y • %I:%M %p"
            )
        except:
            return "Latest"

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_error(self):

        self.clear()

        Label(
            self.root,
            text="Could not load news",
            font=("Helvetica", 14, "bold"),
            bg=self.colors["bg"],
            fg="white"
        ).pack(pady=40)

    def create_button(
        self,
        parent,
        text,
        command,
        color
    ):

        Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            relief="flat",
            bd=0,
            padx=14,
            pady=8,
            font=("Helvetica", 10, "bold"),
            cursor="hand2"
        ).pack(side=LEFT, padx=5)

    def show_news(self):

        self.clear()

        if not self.articles:
            self.show_error()
            return

        article = self.articles[self.index]

        frame = Frame(
            self.root,
            bg=self.colors["bg"]
        )

        frame.pack(
            fill=BOTH,
            expand=True,
            padx=16,
            pady=16
        )

        image = self.fetch_image(
            article.get("urlToImage")
        )

        if image:
            Label(
                frame,
                image=image,
                bg=self.colors["bg"]
            ).pack(pady=(0, 14))

        Label(
            frame,
            text=article.get(
                "title",
                "No title"
            ),
            bg=self.colors["bg"],
            fg=self.colors["text"],
            font=("Helvetica", 15, "bold"),
            wraplength=285,
            justify="left"
        ).pack(anchor="w")

        Label(
            frame,
            text=f'{article.get("source", {}).get("name", "Unknown")} • {self.format_date(article.get("publishedAt", ""))}',
            bg=self.colors["bg"],
            fg=self.colors["muted"],
            font=("Helvetica", 9)
        ).pack(anchor="w", pady=(8, 10))

        Label(
            frame,
            text=article.get("description")
            or "No description available.",
            bg=self.colors["bg"],
            fg="#E4E4E7",
            font=("Helvetica", 11),
            wraplength=285,
            justify="left"
        ).pack(anchor="w")

        nav = Frame(
            self.root,
            bg=self.colors["bg"]
        )
        nav.pack(pady=18)

        if self.index > 0:
            self.create_button(
                nav,
                "← Prev",
                lambda: self.change_news(-1),
                self.colors["blue"]
            )

        self.create_button(
            nav,
            "Read More",
            lambda: webbrowser.open(article["url"]),
            self.colors["green"]
        )

        if self.index < len(self.articles) - 1:
            self.create_button(
                nav,
                "Next →",
                lambda: self.change_news(1),
                self.colors["blue"]
            )

        Label(
            self.root,
            text=f"{self.index + 1} / {len(self.articles)}",
            bg=self.colors["bg"],
            fg=self.colors["muted"],
            font=("Helvetica", 9)
        ).pack(pady=(0, 12))

    def change_news(self, step):
        self.index += step
        self.show_news()


NewsApp()