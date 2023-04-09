class Books_Lib:
    
    def __init__(self,b_id,b_name,b_author,b_published,b_price):
        self.book_id=b_id
        self.book_Name=b_name
        self.book_Author=b_author
        self.book_published=b_published
        self.book_Price=b_price

    def __str__(self):
        return f"Book_ID={self.book_id},Book_Name={self.book_Name},Book_Author={self.book_Author},Book_published={self.book_published},Price={self.book_Price}"

    def getJSONFormatBook(self):
        Books_JSONStructre = {"Book_Id":self.book_id, "name":self.book_Name, "auth_name":self.book_Author,"book_published":self.book_published, "book_Price":self.book_Price}
        return Books_JSONStructre

    
