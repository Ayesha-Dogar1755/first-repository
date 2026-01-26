class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.reviews=[]

    def add_reviews(self,review):
            self.reviews.append(review)
    def count_reviews(self):
            return len(self.reviews)
    def  display_reviews(self):
            for review in self.reviews:
                print(review)

book1=Book("Rich dad,Poor dad","Robert Kiyosaki")
book1.add_reviews("Easy to understand.")
book1.add_reviews("Very informative.")
book1.display_reviews()
print("Total Reviews:",book1.count_reviews())